#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de páginas de produto.

Cada produto é preenchido UMA vez no dicionário PRODUTOS e vira duas páginas:

  solucoes/<slug>.html   com menu, indexada. É a que o Google conhece.
  lp/<slug>.html         sem menu, sem rota de fuga, noindex. É a de campanha.

Mesmo texto, mesma prova, mesmos números. Corrigiu um, corrigiu os dois —
e como a LP fica fora da busca, as duas nunca competem entre si.

Para adicionar um produto: copie um bloco de PRODUTOS, troque o conteúdo,
registre no build.py. Não precisa escrever HTML.

--------------------------------------------------------------------------
IMPORTANTE — a Wicorp é REPRESENTANTE, não operadora.
O link dedicado é entregue sobre a rede de operadoras parceiras. Nenhum texto
aqui pode afirmar rede, backbone ou infraestrutura própria. O diferencial real
é o oposto disso: não estar presa a uma operadora só.
--------------------------------------------------------------------------
"""

from sections import ico

P = "../"

CHECK = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<polyline points="20 6 9 17 4 12"/></svg>')
ARROW = ico('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>', 17, 2.5)

# Ícones da grade de diferenciais
I_REDE    = ('<circle cx="12" cy="12" r="3"/><circle cx="5" cy="5" r="2"/><circle cx="19" cy="5" r="2"/>'
             '<circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><line x1="6.5" y1="6.5" x2="10" y2="10"/>'
             '<line x1="17.5" y1="6.5" x2="14" y2="10"/><line x1="6.5" y1="17.5" x2="10" y2="14"/>'
             '<line x1="17.5" y1="17.5" x2="14" y2="14"/>')
I_LUPA    = '<circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>'
I_CONTRA  = ('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>'
             '<polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/>'
             '<line x1="8" y1="17" x2="13" y2="17"/>')
I_RELOGIO = '<circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/>'
I_ESCUDO  = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>'
I_RAIO    = '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>'
I_ANTENA  = ('<path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/>'
             '<path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/>')
I_FIBRA   = ('<path d="M4 20c0-8 16-8 16-16"/><circle cx="4" cy="20" r="2"/><circle cx="20" cy="4" r="2"/>')


# ===========================================================================
# OS PRODUTOS
# ===========================================================================

PRODUTOS = {}

PRODUTOS["link-dedicado"] = dict(
    # --- identidade ---
    nome="Link Dedicado Empresarial",
    categoria="Conectividade",
    arquivo_solucao="solucoes/link-dedicado-empresarial.html",
    arquivo_lp="lp/link-dedicado.html",

    # --- topo ---
    # H1 da página de solução: carrega a palavra que se busca no Google
    h1_solucao='Link dedicado empresarial com <span class="grad-text">banda garantida e IP fixo</span>',
    # H1 da LP: pergunta que nomeia a dor, no modelo de campanha
    h1_lp='Sua operação depende de sistemas em nuvem, ERP e <span class="grad-text">videoconferência?</span>',
    promessa=("Conectividade estável, velocidade garantida e IP fixo para sua operação, "
              "em fibra óptica ou rádio — conforme a disponibilidade e a necessidade do seu negócio."),
    qualidades=[
        "100% da velocidade contratada, em download e upload",
        "IP fixo e SLA definido em contrato",
        "Fibra óptica ou rádio, conforme o que atende seu endereço",
        "Monitoramento e suporte com equipe própria",
    ],

    # --- um pouco sobre o produto, sem virar aula ---
    sobre_titulo="Sua empresa não pode parar por causa da internet",
    sobre=[
        "Link dedicado não é internet compartilhada. A banda é sua, simétrica, com IP fixo e "
        "prazo de atendimento escrito em contrato.",
        "É o que sustenta ERP, sistemas em nuvem, videoconferência e integrações que não podem "
        "travar no meio do expediente — e é por isso que ele se paga na primeira queda que não aconteceu.",
    ],

    # --- a grade de diferenciais ---
    diferenciais_titulo="Por que contratar com a Wicorp",
    diferenciais=[
        dict(icone=I_REDE, titulo="Independência de operadora",
             texto="Não somos operadora, e isso joga a favor do cliente: trabalhamos com várias "
                   "e indicamos a que realmente atende o seu endereço — não a que precisamos vender."),
        dict(icone=I_LUPA, titulo="Análise antes da proposta",
             texto="Consultamos a viabilidade em fibra e em rádio no endereço da sua operação e "
                   "mostramos o que existe ali. Sem pacote pronto, sem promessa que a obra não cumpre."),
        dict(icone=I_CONTRA, titulo="Um contrato, um interlocutor",
             texto="Link, equipamento, monitoramento e suporte no mesmo contrato. Quando algo "
                   "acontece, você aciona um número — não descobre de quem é a culpa entre quatro fornecedores."),
        dict(icone=I_RELOGIO, titulo="Monitoramento 24/7",
             texto="Nosso NOC acompanha o link continuamente. Na maior parte dos casos a equipe "
                   "já está agindo antes de a falha chegar ao seu usuário."),
        dict(icone=I_ESCUDO, titulo="Redundância que é redundância",
             texto="Fibra e rádio por caminhos independentes, ou link principal somado ao Link.Box "
                   "com dois chips 4G/5G. Dois contratos da mesma operadora caem juntos."),
    ],

    # --- tecnologias / variantes do produto ---
    variantes_titulo="Fibra óptica ou rádio",
    variantes_sub=("A tecnologia certa depende do que existe no seu endereço. A consulta de "
                   "disponibilidade responde isso antes de qualquer proposta."),
    variantes=[
        dict(icone=I_FIBRA, nome="Fibra óptica",
             resumo="Alta capacidade e estabilidade para empresas, indústrias, escritórios e redes de lojas.",
             itens=["IP fixo", "SLA definido em contrato", "Velocidade simétrica",
                    "100% da velocidade contratada"]),
        dict(icone=I_ANTENA, nome="Rádio",
             resumo="Serve como conexão principal ou como redundância, criando um caminho "
                    "alternativo para manter a operação conectada se o link principal falhar.",
             itens=["IP fixo", "SLA definido em contrato", "Velocidade simétrica",
                    "100% da velocidade contratada"]),
    ],
    variantes_fecho=("Combinar tecnologias diferentes reduz o risco de ficar offline: uma falha "
                     "que derruba a fibra raramente derruba o rádio no mesmo instante."),

    # --- formulário ---
    form_titulo="Consulte a disponibilidade",
    form_sub="Informe o endereço da operação e verificamos a viabilidade técnica em fibra e em rádio.",
    form_botao="Consultar disponibilidade",
    form_extras=[
        dict(campo="endereco", rotulo="Endereço onde será instalado o link",
             tipo="text", placeholder="Rua, número, bairro e cidade", obrigatorio=True),
        dict(campo="velocidade", rotulo="Velocidade desejada", tipo="select", obrigatorio=False,
             opcoes=["Não sei — preciso de orientação", "50 Mbps", "100 Mbps", "200 Mbps",
                     "300 Mbps", "500 Mbps", "1 Gbps", "Acima de 1 Gbps"]),
    ],

    # --- fechamento ---
    cta_titulo="Consulte a disponibilidade no seu endereço",
    cta_texto=("Verificamos o que existe de fibra e de rádio no endereço da sua operação antes "
               "de qualquer proposta. Sem compromisso."),
    cta_botao="Consultar disponibilidade",

    # --- perguntas ---
    faq=[
        ("A Wicorp é a operadora do link?",
         "Não. A Wicorp é integradora: o link é entregue sobre a rede de operadoras parceiras, e nós "
         "escolhemos qual delas atende melhor o seu endereço. Na prática, isso significa que não "
         "estamos presos a uma rede só — se a melhor opção ali for outra operadora, é ela que "
         "indicamos. O contrato, o monitoramento e o suporte continuam sendo com a Wicorp."),
        ("Qual a diferença entre link dedicado e banda larga comum?",
         "Banda larga é compartilhada com outros assinantes e a velocidade contratada é um teto, "
         "não uma garantia — no horário de pico ela cai. O link dedicado entrega banda garantida e "
         "simétrica: a mesma velocidade de subida e descida, a qualquer hora, com SLA em contrato."),
        ("Por que preciso de IP fixo?",
         "Sem IP fixo você não consegue publicar serviços próprios, usar VPN com endereço estável, "
         "hospedar câmeras acessíveis de fora nem manter integrações que exigem endereço conhecido. "
         "Para uma empresa, é o que permite tratar a conexão como infraestrutura, não como acesso doméstico."),
        ("Fibra ou rádio: qual escolher?",
         "Fibra é a primeira opção quando existe infraestrutura no endereço — mais estável e com "
         "maior capacidade. Rádio resolve onde a fibra não chegou ou onde a obra civil inviabiliza a "
         "instalação, e a ativação costuma ser mais rápida. A consulta de disponibilidade responde "
         "qual das duas atende o seu endereço."),
        ("O que o SLA garante na prática?",
         "Prazo máximo de atendimento e de solução em caso de falha, além do compromisso de "
         "disponibilidade mensal. É o que separa um contrato empresarial de um plano residencial."),
        ("Em quanto tempo o link é ativado?",
         "Depende da viabilidade técnica no endereço e da operadora que atende ali. Onde já existe "
         "fibra instalada, a ativação costuma ocorrer em poucos dias; em rádio, geralmente é mais "
         "rápido. O prazo exato vai junto com a proposta, não antes dela."),
        ("E se eu já tiver link de outra operadora?",
         "Dá para manter. O Link.Box gerencia múltiplos links, inclusive de operadoras diferentes, "
         "e comuta automaticamente para dois chips 4G/5G quando todos caem. Nesse caso o link que "
         "você já tem vira parte da redundância em vez de ser substituído."),
    ],

    # --- SEO ---
    title="Link Dedicado Empresarial — Fibra ou Rádio com IP Fixo e SLA | Wicorp",
    desc=("Link dedicado empresarial com 100% da velocidade contratada, IP fixo e SLA em contrato. "
          "Fibra óptica ou rádio conforme o seu endereço. Consulte a disponibilidade."),
    title_lp="Link Dedicado Empresarial com banda garantida e IP fixo | Wicorp",
    desc_lp=("Conectividade estável, velocidade garantida e IP fixo para sua operação. "
             "Fibra óptica ou rádio. Consulte a disponibilidade no seu endereço."),
)


# ===========================================================================
# RENDERIZAÇÃO
# ===========================================================================

def _qualidades(p):
    li = "".join(f"<li>{CHECK}<span>{q}</span></li>" for q in p["qualidades"])
    return f'<ul class="checklist">{li}</ul>'


def _sobre(p, alt=False):
    paras = "".join(f"<p>{t}</p>" for t in p["sobre"])
    classe = "section section--alt" if alt else "section"
    return f"""
<section class="{classe}">
  <div class="wrap">
    <div class="section-head reveal" style="max-width:62ch">
      <span class="eyebrow">O que é</span>
      <h2 class="display">{p['sobre_titulo']}</h2>
    </div>
    <div class="prod-sobre reveal">{paras}</div>
  </div>
</section>"""


def _diferenciais(p, alt=True):
    cards = "".join(f"""
      <div class="prod-dif reveal" data-d="{i}">
        <div class="prod-dif__ico">{ico(d['icone'], 26, 1.9)}</div>
        <h3>{d['titulo']}</h3>
        <p>{d['texto']}</p>
      </div>""" for i, d in enumerate(p["diferenciais"]))
    classe = "section section--alt sec-tex" if alt else "section sec-tex"
    return f"""
<section class="{classe}" id="diferenciais">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow" style="margin-inline:auto">Diferenciais</span>
      <h2 class="display">{p['diferenciais_titulo']}</h2>
    </div>
    <div class="prod-difs">{cards}
    </div>
  </div>
</section>"""


def _variantes(p, alt=False):
    if not p.get("variantes"):
        return ""
    cards = "".join(f"""
      <div class="prod-var reveal" data-d="{i}">
        <div class="prod-var__ico">{ico(v['icone'], 24, 2)}</div>
        <h3>{v['nome']}</h3>
        <p>{v['resumo']}</p>
        <ul class="checklist">{"".join(f"<li>{CHECK}<span>{x}</span></li>" for x in v['itens'])}</ul>
      </div>""" for i, v in enumerate(p["variantes"]))
    fecho = (f'<p class="prod-var__fecho reveal">{p["variantes_fecho"]}</p>'
             if p.get("variantes_fecho") else "")
    classe = "section section--alt" if alt else "section"
    return f"""
<section class="{classe}">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow" style="margin-inline:auto">Tecnologias</span>
      <h2 class="display">{p['variantes_titulo']}</h2>
      <p class="lead">{p.get('variantes_sub','')}</p>
    </div>
    <div class="prod-vars">{cards}
    </div>
    {fecho}
  </div>
</section>"""


def corpo_solucao(p, form_html, proof_html, faq_html, cta_html, extra_html=""):
    """Página com menu, indexada — a que responde na busca."""
    return f"""
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        <span class="eyebrow">{p['categoria']}</span>
        <h1 class="display">{p['h1_solucao']}</h1>
        <p class="lead">{p['promessa']}</p>
        {_qualidades(p)}
      </div>
      <div>{form_html}</div>
    </div>
  </div>
</section>

{proof_html}
{_sobre(p, alt=True)}
{_diferenciais(p, alt=False)}
{_variantes(p, alt=True)}
{extra_html}
{faq_html}
{cta_html}
</main>"""


def corpo_lp(p, form_html, faq_html, cta_html):
    """Página de campanha: sem menu, sem link para fora, um objetivo só."""
    return f"""
<main id="main">
<section class="page-hero lp-hero">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        <span class="eyebrow">{p['nome']}</span>
        <h1 class="display">{p['h1_lp']}</h1>
        <p class="lead">{p['promessa']}</p>
        {_qualidades(p)}
      </div>
      <div>{form_html}</div>
    </div>
  </div>
</section>

{_diferenciais(p, alt=True)}
{_variantes(p, alt=False)}
{_sobre(p, alt=True)}
{faq_html}
{cta_html}
</main>"""
