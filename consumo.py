"""
Consumo de banda por link — a matéria-prima do Relatório de Consumo.

Este arquivo é primo do trafego.py, mas responde a outra pergunta.

    trafego.py  -> "como está o link AGORA?"        usa history (5 em 5 min)
    consumo.py  -> "quanto passou no MÊS?"          usa trend  (1 em 1 hora)

Buscar um mês inteiro pelo history traria ~8.900 pontos por item e o
navegador engasgaria desenhando isso. O trend traz 720 e já vem com
mínimo, média e máximo de cada hora calculados pelo próprio Zabbix — que
é exatamente o que um relatório precisa.

Regra do projeto: cálculo mora no service, nunca na view nem no template.
"""

import logging
import math
from datetime import datetime, timezone as fuso_utc

from django.core.cache import cache
from django.utils import timezone

from .trafego import (
    ORDEM_GRAFICOS,
    ROTULO_TIPO,
    TIPO_LATENCIA,
    _escala_agradavel,
    formatar_bps,
    formatar_bps_curto,
)
from .zabbix import ClienteZabbix, ZabbixIndisponivel

logger = logging.getLogger(__name__)


# Relatório olha para o passado fechado — o número de ontem não muda mais.
# Por isso o cache aqui é bem mais longo que o dos painéis ao vivo.
SEGUNDOS_CACHE = 900

# Links de internet contratada. A Rede LAN aparece no relatório, mas fica
# FORA do total de consumo: ela é tráfego interno do cliente, não banda
# contratada da Wicorp. Somar as duas coisas daria um número sem sentido.
TIPOS_WAN = ("principal", "backup", "lte")

# Até este tamanho de período, cada barra é um dia. Acima, vira semana —
# senão um relatório semestral teria 180 barras de 5 pixels cada.
LIMITE_DIAS_POR_BARRA = 45

SEGUNDOS_DIA = 86400
SEGUNDOS_SEMANA = 7 * SEGUNDOS_DIA

# Medidas do desenho. Mais baixo que o gráfico ao vivo porque aqui cabem
# vários links na mesma folha de papel.
LARGURA = 1000
ALTURA = 200
PADDING_TOPO = 10

# Quantas datas aparecem embaixo do gráfico, no máximo.
MAX_ROTULOS_EIXO = 8


# ---------------------------------------------------------------------
# Formatação
# ---------------------------------------------------------------------

def formatar_volume(bits: float) -> str:
    """
    Quantidade de dados trafegados, em bytes.

    O Zabbix mede banda em bits por segundo, mas ninguém fala "consumi 11
    terabits este mês" — o cliente pensa em GB e TB, igual à fatura da
    operadora. Por isso dividimos por 8 antes de mostrar.
    """
    bytes_ = max(bits, 0) / 8
    for limite, sufixo in ((1e12, "TB"), (1e9, "GB"), (1e6, "MB"), (1e3, "KB")):
        if bytes_ >= limite:
            return f"{bytes_ / limite:.2f} {sufixo}"
    return f"{bytes_:.0f} B"


# ---------------------------------------------------------------------
# Contas sobre a série do trend
# ---------------------------------------------------------------------

def _volume_bits(pontos: list[dict]) -> float:
    """
    Quanto passou no período inteiro, em bits.

    Cada ponto do trend é a média de UMA hora, em bits por segundo.
    Média vezes 3600 segundos dá os bits daquela hora; somando as horas,
    sai o volume do período. É a mesma conta que a operadora faz.
    """
    return sum(p["avg"] for p in pontos) * 3600


def _resumir(pontos: list[dict]) -> dict:
    """Mínimo, média, pico e volume de uma direção (download ou upload)."""
    if not pontos:
        return {"minimo": 0.0, "media": 0.0, "maximo": 0.0,
                "volume_bits": 0.0, "tem_dados": False}

    return {
        # Mínimo e pico saem do min/max que o próprio Zabbix guardou dentro
        # de cada hora — não da média horária. Assim o pico do relatório é
        # o pico de verdade, não uma média suavizada.
        "minimo": min(p["min"] for p in pontos),
        "media": sum(p["avg"] for p in pontos) / len(pontos),
        "maximo": max(p["max"] for p in pontos),
        "volume_bits": _volume_bits(pontos),
        "tem_dados": True,
    }


def _tamanho_da_barra(ts_de: int, ts_ate: int) -> tuple[int, str]:
    """Cada barra do gráfico vale um dia ou uma semana, conforme o período."""
    dias = max((ts_ate - ts_de) // SEGUNDOS_DIA, 1)
    if dias <= LIMITE_DIAS_POR_BARRA:
        return SEGUNDOS_DIA, "dia"
    return SEGUNDOS_SEMANA, "semana"


def _medias_por_barra(pontos: list[dict], ts_de: int,
                      tamanho: int, quantas: int) -> list[float]:
    """
    Junta os pontos horários em baldes de dia (ou semana) e tira a média
    de cada balde.

    Média e não soma: assim a barra fica em bits/s, na mesma unidade da
    legenda lateral, e um dia com falha de coleta não vira uma barra baixa
    enganosa — ele vira a média das horas que existem.
    """
    soma = [0.0] * quantas
    contagem = [0] * quantas

    for p in pontos:
        i = (p["clock"] - ts_de) // tamanho
        if 0 <= i < quantas:
            soma[i] += p["avg"]
            contagem[i] += 1

    return [soma[i] / contagem[i] if contagem[i] else 0.0 for i in range(quantas)]


# ---------------------------------------------------------------------
# Desenho (SVG)
# ---------------------------------------------------------------------
#
# ATENÇÃO, a mesma armadilha do trafego.py: todo número que vai virar
# atributo de SVG ou valor de CSS sai daqui como TEXTO já formatado com
# ponto. O projeto está em pt-br e o Django escreveria "199,5" no template;
# SVG e CSS ignoram valor com vírgula, silenciosamente, e o gráfico some.

def _barras(valores: list[float], y_max: float, indice_serie: int) -> list[dict]:
    """
    Retângulos de uma série. Download e upload ficam lado a lado dentro
    do mesmo dia, para dar para comparar os dois de bater o olho.
    """
    quantas = len(valores)
    if not quantas or y_max <= 0:
        return []

    largura_balde = LARGURA / quantas
    largura_barra = largura_balde * 0.32          # 32% + 32% = 64% do dia
    margem = largura_balde * 0.18                 # sobra 18% de cada lado
    util = ALTURA - PADDING_TOPO

    retangulos = []
    for i, valor in enumerate(valores):
        altura = min(valor / y_max, 1.0) * util
        # Um dia de tráfego baixo tem que aparecer como um risquinho, não
        # como buraco: sem isto, "quase zero" fica igual a "sem dados".
        if valor > 0 and altura < 1.5:
            altura = 1.5

        x = largura_balde * i + margem + indice_serie * largura_barra

        retangulos.append({
            "x": f"{x:.2f}",
            "y": f"{ALTURA - altura:.2f}",
            "largura": f"{largura_barra:.2f}",
            "altura": f"{altura:.2f}",
        })
    return retangulos


def _grade(valores_grade: list[float], y_max: float) -> list[dict]:
    """Linhas horizontais com o rótulo de banda de cada uma."""
    if y_max <= 0:
        return []

    util = ALTURA - PADDING_TOPO
    linhas = []
    for valor in valores_grade:
        y = ALTURA - (valor / y_max) * util
        linhas.append({
            "y": f"{y:.1f}",
            "topo_pct": f"{y / ALTURA * 100:.3f}",
            "rotulo": formatar_bps_curto(valor) if valor else "0",
        })
    return linhas


def _rotulos_eixo(ts_de: int, tamanho: int, quantas: int) -> list[dict]:
    """
    As datas embaixo do gráfico, espaçadas para caber.

    No painel ao vivo o Paulo dispensou a legenda de tempo, e faz sentido:
    "últimas 6 horas" é sempre agora. Num relatório de um mês é o contrário
    — sem data não dá para dizer em que dia o consumo subiu.
    """
    if quantas <= 0:
        return []

    passo = max(1, math.ceil(quantas / MAX_ROTULOS_EIXO))
    rotulos = []

    for i in range(0, quantas, passo):
        momento = timezone.localtime(
            datetime.fromtimestamp(ts_de + i * tamanho, tz=fuso_utc.utc)
        )
        rotulos.append({
            "esquerda_pct": f"{(i + 0.5) / quantas * 100:.3f}",
            "texto": momento.strftime("%d/%m"),
        })
    return rotulos


# ---------------------------------------------------------------------
# Montagem de um link
# ---------------------------------------------------------------------

def _montar_link(tipo: str, series: dict, ts_de: int,
                 tamanho: int, quantas: int, unidade_barra: str) -> dict:
    download = _resumir(series["download"])
    upload = _resumir(series["upload"])

    medias_download = _medias_por_barra(series["download"], ts_de, tamanho, quantas)
    medias_upload = _medias_por_barra(series["upload"], ts_de, tamanho, quantas)

    # A escala olha só para as médias diárias — que já são valores suaves.
    # Aqui não precisa do percentil do gráfico ao vivo: a média de um dia
    # inteiro não tem pico isolado de contador SNMP para achatar o resto.
    pico_visivel = max(medias_download + medias_upload + [0.0])
    y_max, valores_grade = _escala_agradavel(pico_visivel * 1.15 or 1.0)

    return {
        "tipo": tipo,
        "rotulo": ROTULO_TIPO.get(tipo, tipo.upper()),
        "eh_wan": tipo in TIPOS_WAN,
        "tem_dados": download["tem_dados"] or upload["tem_dados"],
        "svg": {
            "largura": LARGURA,
            "altura": ALTURA,
            "download": _barras(medias_download, y_max, 0),
            "upload": _barras(medias_upload, y_max, 1),
        },
        "grade": _grade(valores_grade, y_max),
        "eixo": _rotulos_eixo(ts_de, tamanho, quantas),
        "unidade_barra": unidade_barra,
        "download": {
            "minimo": formatar_bps(download["minimo"]),
            "media": formatar_bps(download["media"]),
            "maximo": formatar_bps(download["maximo"]),
            "volume": formatar_volume(download["volume_bits"]),
            "volume_bits": download["volume_bits"],
        },
        "upload": {
            "minimo": formatar_bps(upload["minimo"]),
            "media": formatar_bps(upload["media"]),
            "maximo": formatar_bps(upload["maximo"]),
            "volume": formatar_volume(upload["volume_bits"]),
            "volume_bits": upload["volume_bits"],
        },
        "volume_total": formatar_volume(
            download["volume_bits"] + upload["volume_bits"]
        ),
    }


# ---------------------------------------------------------------------
# Função principal
# ---------------------------------------------------------------------

def relatorio_unidade(unidade, ts_de: int, ts_ate: int) -> dict:
    """
    O consumo de todos os links de UMA unidade no período.

    Uma unidade por chamada, igual ao relatório de disponibilidade: o
    navegador pede de três em três e a tela vai se preenchendo. Fazer as
    500 unidades numa requisição só estouraria o tempo limite.
    """
    if not unidade.zabbix_host_id:
        return {"ok": True, "erro": None, "sem_link": True, "links": []}

    chave = f"consumo:unidade:{unidade.pk}:{ts_de}:{ts_ate}"
    guardado = cache.get(chave)
    if guardado is not None:
        return guardado

    tamanho, unidade_barra = _tamanho_da_barra(ts_de, ts_ate)
    quantas = max(math.ceil((ts_ate - ts_de) / tamanho), 1)

    try:
        with ClienteZabbix() as z:
            itens_por_tipo = z.listar_itens_trafego(unidade.zabbix_host_id)

            links = []
            for tipo in ORDEM_GRAFICOS:
                # A LATÊNCIA NÃO ENTRA NO RELATÓRIO DE CONSUMO.
                #
                # O `ORDEM_GRAFICOS` é compartilhado com o painel ao vivo
                # do trafego.py, e lá a latência TEM tratamento próprio:
                #
                #     if tipo == TIPO_LATENCIA:
                #         links.append(_montar_latencia(par, z, ...))
                #
                # Aqui nunca teve. Então a latência caía no _montar_link(),
                # que espera um par download/upload — e o
                # `listar_itens_trafego` devolve, para ela,
                # {"latencia": {"tempo": ..., "perda": ...}}, sem essas
                # duas chaves. As duas séries voltavam vazias, `tem_dados`
                # ficava False, e o relatório desenhava um cartão
                # "Latência · fora do total" com a hachura de "sem dados".
                #
                # Esse cartão nunca teve dado e nunca teria: latência se
                # mede em milissegundos, não em bits por segundo. Consumo
                # e latência são grandezas diferentes, e o relatório de
                # consumo fala de uma só.
                #
                # Defeito introduzido em 10/09/2026, quando a latência
                # entrou no ORDEM_GRAFICOS para o painel ao vivo. Visto
                # pelo Paulo em 29/09.
                if tipo == TIPO_LATENCIA:
                    continue

                par = itens_por_tipo.get(tipo)
                if not par:
                    continue

                series = {}
                for direcao in ("download", "upload"):
                    item = par.get(direcao)
                    series[direcao] = (
                        z.obter_tendencia(item["itemid"], ts_de, ts_ate)
                        if item else []
                    )

                links.append(
                    _montar_link(tipo, series, ts_de, tamanho, quantas, unidade_barra)
                )

    except ZabbixIndisponivel as erro:
        logger.warning("Consumo indisponível para %s: %s", unidade, erro)
        return {"ok": False, "erro": str(erro), "links": []}

    if not links:
        return {"ok": True, "erro": None, "sem_link": True, "links": []}

    # Total do cliente: só os links de internet. Ver o comentário do
    # TIPOS_WAN lá em cima para o porquê de a Rede LAN ficar de fora.
    wan = [l for l in links if l["eh_wan"]]
    bits_download = sum(l["download"]["volume_bits"] for l in wan)
    bits_upload = sum(l["upload"]["volume_bits"] for l in wan)

    resultado = {
        "ok": True,
        "erro": None,
        "sem_link": False,
        "links": links,
        "tem_lan": any(not l["eh_wan"] for l in links),
        "volume_total": formatar_volume(bits_download + bits_upload),
        "volume_download": formatar_volume(bits_download),
        "volume_upload": formatar_volume(bits_upload),
        "nome": unidade.nome,
    }

    cache.set(chave, resultado, SEGUNDOS_CACHE)
    return resultado
