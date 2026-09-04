#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blog e páginas institucionais.

Os três artigos são os mesmos temas que já existiam no blog antigo,
reescritos seguindo a estrutura do Manual de Copy:
Contexto → Consciência → Educação → Autoridade → Ação.
"""

from sections import ico

WPP_HREF = "551131817756"
TEL, TEL_HREF = "(11) 4800-5000", "+551148005000"

I_CLOUD  = '<path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>'
I_WIFI   = '<path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/>'
I_NET    = '<circle cx="12" cy="12" r="3"/><circle cx="5" cy="5" r="2"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><line x1="6.5" y1="6.5" x2="10" y2="10"/><line x1="17.5" y1="6.5" x2="14" y2="10"/><line x1="6.5" y1="17.5" x2="10" y2="14"/><line x1="17.5" y1="17.5" x2="14" y2="14"/>'
I_CAM    = '<path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/>'
I_TEAM   = '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/>'
I_BOX    = '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/>'

ARROW = ico('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>', 15, 2.5)


def photo_slot(titulo, descricao, ratio="4/3"):
    """Espaço reservado para foto autoral. Sai quando a imagem real entrar."""
    return f"""<div class="photo-slot" style="aspect-ratio:{ratio}">
  <div>
    {ico(I_CAM, 34, 1.6)}
    <span><b>{titulo}</b>{descricao}</span>
  </div>
</div>"""


# ===========================================================================
# ARTIGOS
# ===========================================================================
POSTS = [
    dict(
        slug="pabx-em-nuvem-vale-a-pena",
        cat="Telefonia",
        icone=I_CLOUD,
        titulo="PABX em nuvem: quando vale a pena trocar o aparelho físico",
        h1="PABX em nuvem: quando vale a pena trocar o aparelho físico",
        resumo="A central telefônica na parede ainda funciona. A pergunta não é essa — "
               "é quanto ela custa em coisas que ninguém coloca na planilha.",
        desc="Entenda a diferença entre PABX físico e PABX em nuvem, quando a troca "
             "compensa e o que avaliar antes de decidir. Guia prático para gestores de TI.",
        data="2026-08-14", leitura="6 min",
        toc=[("O que mudou", "mudou"), ("Onde o PABX físico cobra a conta", "custo"),
             ("O que muda na nuvem", "nuvem"), ("Quando a troca não compensa", "quando-nao"),
             ("Como avaliar na prática", "avaliar")],
        corpo="""
<p>Quase toda empresa com mais de dez anos tem uma caixa metálica numa sala técnica
com um emaranhado de cabos saindo dela. Ela funciona. Recebe ligação, distribui ramal,
faz o que sempre fez.</p>

<p>O problema é que a pergunta certa não é <strong>"está funcionando?"</strong>.
É <strong>"quanto essa estrutura está custando em coisas que não aparecem na fatura?"</strong></p>

<h2 id="mudou">O que mudou no atendimento das empresas</h2>

<p>Dez anos atrás, atender bem era atender o telefone. Hoje o cliente chega por WhatsApp,
manda e-mail, abre chat no site e às vezes liga. Se cada canal vive num lugar diferente,
ninguém consegue responder a duas perguntas básicas:</p>

<ul>
  <li>Quantos contatos a gente perdeu ontem?</li>
  <li>Quanto tempo alguém esperou antes de desistir?</li>
</ul>

<p>Uma central física responde sobre ligações. Ela não sabe nada sobre o WhatsApp que
está no celular pessoal do vendedor.</p>

<h2 id="custo">Onde o PABX físico cobra a conta</h2>

<p>Os custos invisíveis costumam aparecer em quatro lugares:</p>

<h3>Cada mudança vira visita técnica</h3>
<p>Contratou alguém novo? Mudou de sala? Precisa de um ramal a mais? Em central física,
isso é chamado, agenda e deslocamento. Em nuvem, é configuração no painel — no mesmo dia.</p>

<h3>Trabalho remoto não estava no projeto</h3>
<p>O aparelho está preso à mesa. Quem trabalha de casa ou está em campo passa a usar o
celular pessoal — e a conversa com o cliente sai do controle da empresa junto.</p>

<h3>Crescer exige projeto novo</h3>
<p>A central foi dimensionada para um número de ramais. Passar disso significa placa nova,
licença nova e, às vezes, equipamento novo.</p>

<h3>Não existe relatório</h3>
<p>Sem dado, a gestão do atendimento vira percepção. "Acho que está tranquilo" não é
informação sobre a qual dá para decidir.</p>

<blockquote>Uma conexão instável pode comprometer sistemas, atendimentos, pagamentos
e a produtividade das equipes. Com telefonia acontece o mesmo — só que de forma
mais silenciosa.</blockquote>

<h2 id="nuvem">O que muda com o PABX em nuvem</h2>

<p>A central deixa de ser um equipamento e passa a ser um serviço. Na prática:</p>

<ul>
  <li><strong>O ramal vai junto com a pessoa</strong> — funciona no celular e no computador, com o mesmo número</li>
  <li><strong>Ajuste é imediato</strong> — criar, mover ou remover ramal leva minutos, no painel</li>
  <li><strong>Os canais se juntam</strong> — ligação, WhatsApp e chat na mesma fila, com histórico da empresa</li>
  <li><strong>Existe relatório</strong> — chamadas atendidas, perdidas, tempo de espera, desempenho por fila</li>
  <li><strong>A numeração é sua</strong> — a portabilidade mantém os números que o mercado já conhece</li>
</ul>

<p>Recursos de inteligência artificial entram nesse ponto: URA que entende o assunto e
encaminha direto para quem resolve, transcrição de chamada, resumo de atendimento.
Não é enfeite — é o que reduz transferência desnecessária.</p>

<h2 id="quando-nao">Quando a troca não compensa</h2>

<p>Ser honesto aqui evita frustração depois. A migração tende a <strong>não</strong> valer
a pena quando:</p>

<ul>
  <li>A central física foi instalada há pouco tempo e ainda está no ciclo de investimento</li>
  <li>A operação tem poucos ramais, volume baixo e nenhuma demanda de mobilidade</li>
  <li>A conexão de internet do local é instável e não há plano de redundância</li>
</ul>

<p>Este último ponto merece atenção. Telefonia em nuvem depende de internet. Numa operação
crítica, faz sentido tratar as duas coisas juntas: migrar a telefonia e, na mesma conversa,
resolver a redundância do link. Foi para isso que existe o
<a href="../solucoes/link-dedicado-empresarial.html">backup automático 4G/5G</a>.</p>

<h2 id="avaliar">Como avaliar na prática</h2>

<p>Antes de pedir proposta para qualquer fornecedor, levante quatro números:</p>

<ol>
  <li><strong>Quantos ramais</strong> a empresa usa hoje, e quantos usaria se não houvesse limitação</li>
  <li><strong>Quanto se gasta por mês</strong> com a operadora atual, somando linhas, manutenção e chamados</li>
  <li><strong>Quantas pessoas</strong> precisam atender fora do escritório</li>
  <li><strong>Quais canais</strong> o cliente já usa para falar com vocês</li>
</ol>

<p>Com esses quatro números, qualquer comparação entre fornecedores fica objetiva.
Sem eles, a conversa vira disputa de preço por ramal — que é o pior critério possível
para uma decisão de infraestrutura.</p>
""",
        cta_titulo="Quer dimensionar sua operação?",
        cta_texto="Ajuste o número de ramais e veja a configuração que costumamos recomendar "
                  "para uma operação desse porte.",
        cta_botao="Dimensionar minha operação",
        cta_href="../solucoes/pabx-virtual-nuvem.html#dimensionar",
    ),

    dict(
        slug="link-box-redundancia-internet",
        cat="Conectividade",
        icone=I_WIFI,
        titulo="Link.Box: como funciona a redundância de internet com dois chips 4G/5G",
        h1="Link.Box: como funciona a redundância de internet com dois chips 4G/5G",
        resumo="Contratar dois links da mesma operadora não é redundância. "
               "Este texto explica a diferença — e o que acontece quando a fibra cai de verdade.",
        desc="Como funciona a redundância de internet do Link.Box: comutação automática para "
             "dois chips 4G/5G quando a conexão principal falha. Sem intervenção da equipe.",
        data="2026-08-06", leitura="7 min",
        toc=[("O ponto único de falha", "ponto-unico"), ("Por que dois links não bastam", "dois-links"),
             ("Como o Link.Box funciona", "como-funciona"), ("O que acontece na queda", "na-queda"),
             ("Para quem faz mais diferença", "para-quem")],
        corpo="""
<p>Toda empresa descobre que não tinha plano B no mesmo dia: aquele em que a internet cai
às dez da manhã de uma terça-feira e o time inteiro fica olhando para a tela.</p>

<p>O prejuízo raramente é o valor do link. É o PDV que parou de faturar, a filial isolada,
o sistema em nuvem inacessível e o cliente que ligou e não foi atendido.</p>

<h2 id="ponto-unico">O ponto único de falha</h2>

<p>A maior parte das operações depende de uma única conexão. Quando ela falha —
por rompimento de fibra, manutenção da operadora ou problema no equipamento —
não existe caminho alternativo. A operação simplesmente para até alguém consertar.</p>

<p>E aqui está o detalhe incômodo: <strong>o tempo de reparo não está sob seu controle</strong>.
O SLA da operadora define um prazo máximo, não um prazo real. Quatro horas de contrato
podem ser quatro horas de loja parada.</p>

<h2 id="dois-links">Por que dois links da mesma operadora não bastam</h2>

<p>A solução intuitiva é contratar um segundo link. Ela ajuda — mas menos do que parece,
por um motivo simples: se os dois links são da mesma operadora, eles frequentemente
compartilham a mesma infraestrutura no caminho.</p>

<p>Uma retroescavadeira que rompe a fibra na rua leva os dois juntos. A manutenção
programada da operadora derruba os dois juntos. Você pagou por dois links e continua
com um ponto único de falha, só que mais caro.</p>

<blockquote>Redundância de verdade exige caminhos independentes. Não basta ter dois
cabos: eles precisam depender de coisas diferentes.</blockquote>

<h2 id="como-funciona">Como o Link.Box funciona</h2>

<p>O Link.Box é o equipamento que a Wicorp desenvolveu para resolver exatamente isso.
Ele gerencia diferentes conexões ao mesmo tempo e monitora a principal continuamente.</p>

<p>A estrutura tem três camadas:</p>

<ul>
  <li><strong>Link principal</strong> — a fibra dedicada, com banda garantida e IP fixo</li>
  <li><strong>Backup 5G</strong> — chip de uma operadora móvel, em espera</li>
  <li><strong>Backup 4G</strong> — chip de uma <em>segunda</em> operadora, como terceira camada</li>
</ul>

<p>O ponto que importa: as três rotas são independentes. A fibra passa pelo cabo,
os chips passam por torres de operadoras diferentes. Uma falha que derruba uma delas
não derruba as outras.</p>

<h2 id="na-queda">O que acontece quando a fibra cai</h2>

<p>A sequência é sempre a mesma, e leva pouco mais de um segundo:</p>

<ol>
  <li>O Link.Box detecta que a conexão principal parou de responder</li>
  <li>Confirma a falha em três tentativas, para não comutar por oscilação passageira</li>
  <li>Migra o tráfego para o chip 5G automaticamente</li>
  <li>Deixa o 4G pronto como segunda camada de contingência</li>
  <li>Avisa o NOC, que passa a acompanhar o caso</li>
  <li>Quando a fibra volta, devolve o tráfego para ela</li>
</ol>

<p><strong>Ninguém da sua equipe precisa fazer nada.</strong> Não há chamado para abrir,
cabo para trocar ou roteador para reiniciar. Na maioria dos casos, o usuário final
nem percebe que houve troca.</p>

<p>Você pode ver essa sequência acontecendo na
<a href="../solucoes/link-dedicado-empresarial.html#failover">simulação da página do Link.Box</a> —
é a mesma que rodamos em campo antes de entregar qualquer projeto.</p>

<h2 id="para-quem">Para quem isso faz mais diferença</h2>

<p>Redundância é seguro: só parece cara até o dia em que você precisa dela.
Mas há operações em que ela deixa de ser opcional:</p>

<ul>
  <li><strong>Redes de varejo e farmácias</strong> — um PDV sem conexão não emite fiscal nem processa pagamento</li>
  <li><strong>Operações com várias filiais</strong> — a unidade isolada perde acesso a sistema, telefonia e ao restante da empresa</li>
  <li><strong>Indústrias</strong> — sistemas de produção e apontamento param junto</li>
  <li><strong>Operações de atendimento</strong> — telefonia em nuvem cai junto com a internet</li>
  <li><strong>Empresas com ERP em nuvem</strong> — sem link, não há sistema</li>
</ul>

<p>A conta que vale fazer é simples: quanto sua empresa deixa de faturar por hora parada?
Fizemos uma <a href="../calculadora-custo-downtime.html">calculadora para isso</a> — coloque os números da sua operação e compare com o custo mensal da camada de redundância. Na maioria dos casos, uma única
ocorrência evitada paga o ano.</p>
""",
        cta_titulo="Sua operação tem plano B?",
        cta_texto="Avaliamos sua estrutura atual e mostramos onde existe ponto único de falha. "
                  "Sem compromisso.",
        cta_botao="Solicitar avaliação da minha rede",
        cta_href="../solucoes/link-dedicado-empresarial.html#form",
    ),

    dict(
        slug="sd-wan-reduzir-custo-link",
        cat="Segurança e redes",
        icone=I_NET,
        titulo="SD-WAN: como reduzir custo de link sem perder estabilidade",
        h1="SD-WAN: como reduzir custo de link sem perder estabilidade",
        resumo="Empresas com várias unidades costumam pagar caro por links que usam mal. "
               "O SD-WAN resolve isso decidindo, em tempo real, o que passa por onde.",
        desc="O que é SD-WAN, como ele distribui o tráfego entre links disponíveis e por que "
             "reduz custo em operações com várias unidades sem comprometer a estabilidade.",
        data="2026-07-22", leitura="6 min",
        toc=[("O problema das várias unidades", "problema"), ("O que o SD-WAN faz", "o-que-faz"),
             ("Onde entra a economia", "economia"), ("A parte de segurança", "seguranca"),
             ("O que avaliar antes", "avaliar")],
        corpo="""
<p>Uma empresa com oito filiais costuma ter oito contratos de link, oito faturas e
nenhuma visão do conjunto. Cada unidade contratou o que conseguiu na região,
em momentos diferentes, com quem apareceu primeiro.</p>

<p>O resultado é previsível: algumas unidades pagam caro por banda que sobra,
outras vivem no limite, e ninguém sabe dizer onde está o gargalo.</p>

<h2 id="problema">O problema das operações com várias unidades</h2>

<p>Quando cada unidade é uma ilha, três coisas acontecem:</p>

<h3>O tráfego crítico disputa espaço com o resto</h3>
<p>A videoconferência da diretoria compete com atualização de sistema operacional
e com streaming que ninguém autorizou. Todos passam pelo mesmo cano,
com a mesma prioridade.</p>

<h3>A política de segurança varia por unidade</h3>
<p>Cada filial tem seu equipamento, sua regra e seu nível de atualização.
Uma unidade mal configurada vira porta de entrada para toda a rede.</p>

<h3>Ninguém enxerga o conjunto</h3>
<p>Sem visão centralizada, a decisão de aumentar banda é feita por reclamação:
a unidade que grita mais alto ganha upgrade — não necessariamente a que precisa.</p>

<h2 id="o-que-faz">O que o SD-WAN faz, sem jargão</h2>

<p>SD-WAN significa rede de longa distância definida por software. Traduzindo:
em vez de o caminho do tráfego ser fixo no equipamento, ele passa a ser decidido
por regras que você define — e ajustado em tempo real conforme a condição de cada link.</p>

<p>Na prática, o SD-WAN observa continuamente latência, perda de pacote e
disponibilidade de cada conexão, e roteia cada tipo de tráfego pelo caminho
que faz mais sentido naquele momento:</p>

<ul>
  <li>Voz e videoconferência pelo link mais estável</li>
  <li>Acesso ao ERP com prioridade garantida</li>
  <li>Backup e atualização pelo link secundário, fora do horário de pico</li>
  <li>Tráfego não corporativo por último — ou bloqueado</li>
</ul>

<h2 id="economia">Onde entra a economia</h2>

<p>A economia não vem de contratar link mais barato. Vem de três lugares:</p>

<ol>
  <li><strong>Usar o que já existe</strong> — em vez de dobrar a banda de um link caro,
  o SD-WAN combina o link principal com uma conexão secundária mais barata e distribui o tráfego</li>
  <li><strong>Parar de dimensionar pelo pico</strong> — com priorização, você não precisa
  contratar banda para o pior cenário simultâneo</li>
  <li><strong>Reduzir chamado</strong> — problema de lentidão que hoje vira ticket
  passa a ser resolvido por regra</li>
</ol>

<p>Vale ser honesto: SD-WAN não é mágica de corte de custo. Em operações pequenas,
com uma unidade só, o ganho raramente justifica. Ele brilha quando há
<strong>várias unidades e tráfego heterogêneo</strong>.</p>

<h2 id="seguranca">A parte de segurança que costuma passar batido</h2>

<p>O SD-WAN quase sempre chega junto com o firewall — e é aí que a conversa fica
mais interessante para quem responde por risco.</p>

<p>Com política única aplicada a todas as unidades, você passa a ter:</p>

<ul>
  <li>A mesma regra de segurança valendo em toda a rede, não uma por filial</li>
  <li>Segmentação — um incidente numa unidade não se propaga para as outras</li>
  <li>Registro centralizado de eventos, que é o que sustenta uma resposta a incidente
  e as exigências da LGPD</li>
  <li>Visibilidade de qual aplicação consome o quê, em cada ponto</li>
</ul>

<p>Esse conjunto está detalhado na página de
<a href="../solucoes/firewall-sd-wan.html">firewall e SD-WAN</a>.</p>

<h2 id="avaliar">O que avaliar antes de contratar</h2>

<p>Três perguntas separam uma boa proposta de uma cara:</p>

<ol>
  <li><strong>Quem gerencia depois?</strong> Equipamento entregue sem gestão vira appliance
  esquecido com firmware de três anos. Confirme se a operação está inclusa</li>
  <li><strong>O que acontece quando um link cai?</strong> O SD-WAN deve continuar operando
  com o que sobrou, não parar junto</li>
  <li><strong>Que relatório você recebe?</strong> Se não houver relatório periódico,
  você não tem como saber se está funcionando</li>
</ol>

<p>E um lembrete que vale para qualquer projeto de rede: comece pelo diagnóstico
da estrutura atual. Boa parte das empresas descobre, no levantamento, que já paga
por links que ninguém está usando direito.</p>
""",
        cta_titulo="Vamos olhar sua rede antes de propor qualquer coisa",
        cta_texto="Avaliamos a exposição da sua estrutura e entregamos um relatório com os "
                  "pontos que precisam de atenção.",
        cta_botao="Solicitar diagnóstico de cibersegurança",
        cta_href="../solucoes/firewall-sd-wan.html#form",
    ),
]


def _fmt(d):
    m = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]
    a, mm, dd = d.split("-")
    return f"{int(dd)} de {m[int(mm)-1]} de {a}"


def post_body(p, outros):
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for t, i in p["toc"])
    rel = "".join(f"""
      <a class="post-card" href="{o['slug']}.html">
        <div class="post-card__cover">{ico(o['icone'], 46, 1.4)}</div>
        <div class="post-card__body">
          <div class="post-card__meta"><span class="post-card__cat">{o['cat']}</span><span>·</span><span>{o['leitura']}</span></div>
          <h3>{o['titulo']}</h3>
          <span class="post-card__cta">Ler o artigo completo {ARROW}</span>
        </div>
      </a>""" for o in outros)

    return f"""
<main id="main">
<article>
<section class="page-hero" style="padding-bottom:44px">
  <div class="wrap">
    <div class="article">
      <nav class="crumb" aria-label="Você está em">
        <a href="../index.html">Início</a>
        {ico('<polyline points="9 18 15 12 9 6"/>', 12, 2.5)}
        <a href="index.html">Blog</a>
        {ico('<polyline points="9 18 15 12 9 6"/>', 12, 2.5)}
        <span>{p['cat']}</span>
      </nav>
      <span class="eyebrow">{p['cat']}</span>
      <h1 class="display" style="margin-bottom:20px">{p['h1']}</h1>
      <p class="lead">{p['resumo']}</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="article">
      <div class="article__meta">
        <span>Publicado em {_fmt(p['data'])}</span><span class="dot"></span>
        <span>{p['leitura']} de leitura</span><span class="dot"></span>
        <span>Por Wicorp</span>
      </div>

      <nav class="toc" aria-label="Neste artigo">
        <b>Neste artigo</b>
        <ul>{toc}</ul>
      </nav>

      <div class="prose">{p['corpo']}</div>

      <div class="article__share">
        <span>Achou útil? Compartilhe com quem cuida da TI da sua empresa.</span>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight" style="padding-top:0">
  <div class="wrap">
    <div class="article">
      <div class="cta-band">
        <div class="cta-band__inner">
          <div>
            <h2 class="display">{p['cta_titulo']}</h2>
            <p class="lead">{p['cta_texto']}</p>
          </div>
          <div class="cta-band__actions">
            <a href="{p['cta_href']}" class="btn btn--primary btn--wide">{p['cta_botao']} {ARROW}</a>
            <a href="https://wa.me/{WPP_HREF}" data-pos="artigo" class="btn btn--ghost btn--wide" target="_blank" rel="noopener">Falar no WhatsApp</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Continue lendo</span>
      <h2 class="display">Outros artigos</h2>
    </div>
    <div class="grid grid--2">{rel}</div>
  </div>
</section>
</article>
</main>
"""


def blog_index():
    cards = "".join(f"""
      <a class="post-card reveal" href="{p['slug']}.html">
        <div class="post-card__cover">{ico(p['icone'], 54, 1.3)}</div>
        <div class="post-card__body">
          <div class="post-card__meta">
            <span class="post-card__cat">{p['cat']}</span><span>·</span>
            <span>{_fmt(p['data'])}</span><span>·</span><span>{p['leitura']}</span>
          </div>
          <h3>{p['titulo']}</h3>
          <p>{p['resumo']}</p>
          <span class="post-card__cta">Ler o artigo completo {ARROW}</span>
        </div>
      </a>""" for p in POSTS)

    return f"""
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Conteúdo para quem cuida da operação</span>
    <h1 class="display" style="max-width:20ch">Blog <span class="grad-text">Wicorp</span></h1>
    <p class="lead" style="max-width:58ch">
      Conectividade, telefonia e segurança explicadas sem jargão — para o gestor decidir
      com informação, não com achismo.
    </p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--3">{cards}</div>
  </div>
</section>

<section class="section section--alt section--tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <div class="cta-band__inner">
        <div>
          <h2 class="display">Prefere conversar sobre o seu caso?</h2>
          <p class="lead">
            Artigo ajuda a entender o cenário. Para saber o que se aplica à sua operação,
            uma conversa de 20 minutos resolve mais.
          </p>
        </div>
        <div class="cta-band__actions">
          <a href="../contato.html" class="btn btn--primary btn--wide">Falar com um especialista {ARROW}</a>
          <a href="tel:{TEL_HREF}" class="btn btn--ghost btn--wide">Ligar: {TEL}</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""


# ===========================================================================
# QUEM SOMOS
# ===========================================================================
QUEM_SOMOS = f"""
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        <span class="eyebrow">Desde 1998</span>
        <h1 class="display">Transformar tecnologia em <span class="grad-text">conexão estratégica</span></h1>
        <p class="lead">
          A Wicorp nasceu em 1998 com um propósito claro. Vinte e oito anos depois,
          atendemos mais de 800 empresas e mantemos cerca de 700 equipamentos em operação —
          a maior parte em operações que não podem parar.
        </p>
        <div class="hero__actions">
          <a href="contato.html" class="btn btn--primary">Falar com um especialista {ARROW}</a>
          <a href="index.html#solucoes" class="btn btn--ghost">Ver soluções</a>
        </div>
      </div>
      <div>
        {photo_slot("Foto da equipe Wicorp", "Espaço reservado para imagem autoral. Entra em img/equipe.jpg sem alterar o layout.")}
      </div>
    </div>
  </div>
</section>

<section class="proof">
  <div class="wrap">
    <div class="proof__grid">
      <div class="proof__item"><div class="proof__num grad-text" data-count="28">0</div><div class="proof__lbl">anos de mercado<br>desde 1998</div></div>
      <div class="proof__item"><div class="proof__num grad-text" data-count="800" data-prefix="+">0</div><div class="proof__lbl">clientes ativos<br>em todo o Brasil</div></div>
      <div class="proof__item"><div class="proof__num grad-text" data-count="700" data-prefix="+">0</div><div class="proof__lbl">equipamentos<br>em operação</div></div>
      <div class="proof__item"><div class="proof__num grad-text">24/7</div><div class="proof__lbl">monitoramento<br>proativo da rede</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <span class="eyebrow">Como trabalhamos</span>
        <h2 class="display" style="margin-bottom:20px">Não apenas instalamos tecnologia. Desenhamos soluções.</h2>
        <p class="lead" style="margin-bottom:16px">
          A diferença entre um fornecedor e um parceiro aparece no dia do problema.
          Fornecedor entrega o que foi contratado. Parceiro conhece o ambiente inteiro
          e sabe onde olhar primeiro.
        </p>
        <p class="lead muted">
          É por isso que atuamos como extensão da área de TI dos nossos clientes:
          assumimos a complexidade da infraestrutura para que o gestor recupere tempo
          para o que é estratégico.
        </p>
      </div>
      <div class="callout">
        <h3>Por que só São Paulo e Grande São Paulo</h3>
        <p>Poderíamos vender para o Brasil inteiro. Não vendemos — porque SLA que não se
        cumpre não é SLA, é texto em contrato.</p>
        <p>Concentramos a operação onde conseguimos garantir suporte presencial,
        monitoramento e tempo de resposta. A expansão acontece de forma seletiva,
        quando conseguimos manter o mesmo padrão.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <span class="eyebrow">Nossa trajetória</span>
        <h2 class="display" style="margin-bottom:34px">De provedor a parceiro de tecnologia</h2>
        <ul class="timeline">
          <li>
            <b>1998</b>
            <h3>O começo</h3>
            <p>A Wicorp nasce em São Paulo com foco em telecomunicações corporativas,
            num momento em que conectividade empresarial ainda era exceção.</p>
          </li>
          <li>
            <b>2010s</b>
            <h3>Ampliação do ecossistema</h3>
            <p>Telefonia, segurança e infraestrutura entram no portfólio. A empresa deixa
            de vender serviços isolados e passa a desenhar ambientes completos.</p>
          </li>
          <li>
            <b>Link.Box</b>
            <h3>Tecnologia própria</h3>
            <p>Desenvolvemos a solução de redundância com dois chips 4G/5G para resolver
            um problema que nenhum fornecedor resolvia bem: continuidade real quando a fibra cai.</p>
          </li>
          <li>
            <b>wcloud</b>
            <h3>Comunicação em nuvem com IA</h3>
            <p>PABX virtual, Contact Center e atendimento multicanal integrados,
            com recursos de inteligência artificial aplicados ao atendimento.</p>
          </li>
          <li>
            <b>Hoje</b>
            <h3>Mais de 800 empresas</h3>
            <p>Redes de varejo, farmácias, indústrias, hospitais e instituições de ensino —
            operações críticas que dependem de estar conectadas.</p>
          </li>
        </ul>
      </div>
      <div>
        {photo_slot("NOC 24/7 em operação", "A prova de que o monitoramento proativo existe. Entra em img/noc.jpg.", "3/4")}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">O que nos guia</span>
      <h2 class="display">Missão, visão e valores</h2>
    </div>
    <div class="grid grid--3">
      <div class="card reveal">
        <h3 style="font-size:1.1rem;margin-bottom:10px">Missão</h3>
        <p style="font-size:.94rem;color:var(--tx-2);line-height:1.7">
          Integrar soluções de TIC que fortalecem a comunicação e impulsionam resultados.
        </p>
      </div>
      <div class="card reveal" data-d="1">
        <h3 style="font-size:1.1rem;margin-bottom:10px">Visão</h3>
        <p style="font-size:.94rem;color:var(--tx-2);line-height:1.7">
          Ser referência em soluções de comunicação corporativa inovadoras e estratégicas.
        </p>
      </div>
      <div class="card reveal" data-d="2">
        <h3 style="font-size:1.1rem;margin-bottom:10px">Valores</h3>
        <p style="font-size:.94rem;color:var(--tx-2);line-height:1.7">
          Inovação, excelência técnica, transparência, compromisso com resultados
          e parceria de longo prazo.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt section--tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <div class="cta-band__inner">
        <div>
          <h2 class="display">Vamos conversar sobre sua operação</h2>
          <p class="lead">
            Avaliamos sua estrutura atual e mostramos onde existe ponto único de falha,
            o que dá para centralizar e onde está o retrabalho do seu time.
          </p>
        </div>
        <div class="cta-band__actions">
          <a href="contato.html" class="btn btn--primary btn--wide">Solicitar uma avaliação {ARROW}</a>
          <a href="tel:{TEL_HREF}" class="btn btn--ghost btn--wide">Ligar: {TEL}</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""


# ===========================================================================
# POLÍTICA DE PRIVACIDADE
# ===========================================================================
PRIVACIDADE = """
<main id="main">
<section class="page-hero" style="padding-bottom:40px">
  <div class="wrap">
    <div class="article">
      <span class="eyebrow">Transparência</span>
      <h1 class="display" style="margin-bottom:18px">Política de Privacidade</h1>
      <p class="lead">
        Como a Wicorp trata os dados pessoais coletados neste site, conforme a
        Lei Geral de Proteção de Dados (Lei 13.709/2018).
      </p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="article">

      <div class="callout" style="margin-bottom:38px">
        <h3>Antes de publicar</h3>
        <p>Este documento é uma base preparada a partir das exigências da LGPD e do que
        o site efetivamente coleta. <strong>Ele precisa de revisão do jurídico da Wicorp
        antes de ir ao ar</strong> — principalmente os prazos de retenção, a base legal
        de cada tratamento e a indicação do encarregado.</p>
        <p>Os campos marcados como <strong>[a definir]</strong> dependem de decisão interna.</p>
      </div>

      <div class="prose">
        <p class="muted" style="font-size:.9rem">Última atualização: [a definir]</p>

        <h2 id="quem">1. Quem somos</h2>
        <p>A Wicorp — Conexões Inteligentes, inscrita no CNPJ <strong>[a definir]</strong>,
        com sede na Av. Luiz Dumont Villares, 2078 — CJ 78, Parada Inglesa, São Paulo — SP,
        02239-000, é a controladora dos dados pessoais tratados neste site.</p>

        <h2 id="dados">2. Quais dados coletamos</h2>
        <p>Coletamos apenas o necessário para responder ao seu contato:</p>
        <ul>
          <li><strong>Dados que você informa</strong> — nome, e-mail corporativo, empresa e
          telefone/WhatsApp, quando preenche um formulário</li>
          <li><strong>Dados de navegação</strong> — páginas visitadas, tempo de permanência,
          origem do acesso e tipo de dispositivo, coletados por ferramentas de análise</li>
          <li><strong>Cookies</strong> — arquivos que permitem lembrar preferências e medir
          o desempenho do site</li>
        </ul>
        <p>Não coletamos dados sensíveis, e não solicitamos CPF, CNPJ ou informação
        financeira em formulários deste site.</p>

        <h2 id="finalidade">3. Para que usamos</h2>
        <ol>
          <li>Responder à sua solicitação de contato, proposta ou avaliação técnica</li>
          <li>Enviar informações sobre soluções que tenham relação com o que você pediu</li>
          <li>Entender como o site é usado, para melhorá-lo</li>
          <li>Cumprir obrigações legais e regulatórias</li>
        </ol>

        <h2 id="base">4. Base legal</h2>
        <p>O tratamento se apoia em:</p>
        <ul>
          <li><strong>Consentimento</strong> — quando você preenche um formulário por
          vontade própria</li>
          <li><strong>Legítimo interesse</strong> — para análise de navegação e melhoria
          do site, sempre respeitando seus direitos</li>
          <li><strong>Execução de contrato</strong> — quando o contato evolui para uma
          relação comercial</li>
        </ul>

        <h2 id="compartilha">5. Com quem compartilhamos</h2>
        <p>Não vendemos nem cedemos seus dados. O compartilhamento ocorre apenas com:</p>
        <ul>
          <li>Ferramentas de gestão comercial e de análise que utilizamos para operar,
          sempre sob contrato e com obrigação de confidencialidade</li>
          <li>Autoridades públicas, quando houver exigência legal</li>
        </ul>

        <h2 id="retencao">6. Por quanto tempo guardamos</h2>
        <p>Mantemos os dados pelo tempo necessário às finalidades acima ou pelo prazo
        exigido por lei. Prazo definido: <strong>[a definir]</strong>.</p>
        <p>Encerrada a finalidade, os dados são eliminados ou anonimizados.</p>

        <h2 id="direitos">7. Seus direitos</h2>
        <p>A LGPD garante a você o direito de:</p>
        <ul>
          <li>Confirmar se tratamos seus dados e acessá-los</li>
          <li>Corrigir dados incompletos ou desatualizados</li>
          <li>Solicitar anonimização, bloqueio ou eliminação</li>
          <li>Solicitar a portabilidade a outro fornecedor</li>
          <li>Revogar o consentimento a qualquer momento</li>
          <li>Saber com quem compartilhamos seus dados</li>
        </ul>
        <p>Para exercer qualquer um deles, escreva para
        <a href="mailto:comercial@wicorp.com.br">comercial@wicorp.com.br</a>.
        Respondemos em até 15 dias.</p>

        <h2 id="seguranca">8. Segurança</h2>
        <p>Adotamos medidas técnicas e administrativas para proteger os dados contra acesso
        não autorizado, perda ou alteração — incluindo controle de acesso, criptografia em
        trânsito e monitoramento da infraestrutura.</p>

        <h2 id="cookies">9. Cookies</h2>
        <p>Você pode bloquear ou apagar cookies nas configurações do seu navegador.
        Isso pode afetar o funcionamento de partes do site.</p>

        <h2 id="encarregado">10. Encarregado de dados</h2>
        <p>Encarregado (DPO): <strong>[a definir]</strong><br>
        Contato: <a href="mailto:comercial@wicorp.com.br">comercial@wicorp.com.br</a></p>

        <h2 id="mudancas">11. Mudanças nesta política</h2>
        <p>Podemos atualizar este documento. A data de atualização no topo sempre indica
        a versão vigente.</p>
      </div>
    </div>
  </div>
</section>
</main>
"""


# ===========================================================================
# 404
# ===========================================================================
NAO_ENCONTRADA = f"""
<main id="main">
<section class="err">
  <div class="wrap" style="max-width:620px">
    <div class="err__code">404</div>
    <h1 class="display" style="margin-bottom:16px">Esta página não existe</h1>
    <p class="lead" style="margin-bottom:32px">
      O endereço pode ter mudado ou o link estar incorreto.
      Abaixo estão os caminhos mais procurados.
    </p>

    <div class="hero__actions" style="justify-content:center; margin-bottom:44px">
      <a href="index.html" class="btn btn--primary">Voltar para a home {ARROW}</a>
      <a href="contato.html" class="btn btn--ghost">Falar com um especialista</a>
    </div>

    <div class="grid grid--2" style="text-align:left">
      <a class="card" href="solucoes/link-dedicado-empresarial.html">
        <h3 style="font-size:1rem;margin-bottom:6px">Link dedicado e Link.Box</h3>
        <p style="font-size:.86rem;color:var(--tx-3)">Conexão com backup automático 4G/5G</p>
      </a>
      <a class="card" href="solucoes/pabx-virtual-nuvem.html">
        <h3 style="font-size:1rem;margin-bottom:6px">PABX virtual com IA</h3>
        <p style="font-size:.86rem;color:var(--tx-3)">Telefonia e atendimento em nuvem</p>
      </a>
      <a class="card" href="solucoes/firewall-sd-wan.html">
        <h3 style="font-size:1rem;margin-bottom:6px">Firewall e SD-WAN</h3>
        <p style="font-size:.86rem;color:var(--tx-3)">Proteção de rede gerenciada</p>
      </a>
      <a class="card" href="blog/index.html">
        <h3 style="font-size:1rem;margin-bottom:6px">Blog</h3>
        <p style="font-size:.86rem;color:var(--tx-3)">Conteúdo para quem cuida da operação</p>
      </a>
    </div>
  </div>
</section>
</main>
"""


# ===========================================================================
# CALCULADORA DE CUSTO DE DOWNTIME
#
# Ideia vinda do material da Gonçalves Rauber ("Calcular Custo de Downtime da
# Sua Operação", nas recomendações de CTA e no Banco de Copy). Lá era um
# infográfico estático; aqui virou calculadora — o visitante usa o número
# da própria empresa.
#
# Não exibe preço da solução Wicorp: o posicionamento é proposta
# personalizada, e comparar com valor inventado seria desonesto.
# ===========================================================================
CALCULADORA = f"""
<main id="main">
<section class="page-hero" style="padding-bottom:40px">
  <div class="wrap">
    <span class="eyebrow">Calculadora · sem cadastro</span>
    <h1 class="display" style="max-width:22ch">Quanto custa uma hora da sua operação <span class="grad-text">parada?</span></h1>
    <p class="lead" style="max-width:62ch">
      Preencha com os números da sua empresa e veja o que a indisponibilidade custa por mês
      e por ano. O cálculo acontece aqui no seu navegador — nada é enviado.
    </p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="calc">

      <div class="calc__form">

        <div class="calc__field">
          <label class="calc__label" for="c-fat">
            <span>Faturamento mensal da operação</span>
          </label>
          <div class="field calc__money" style="margin-bottom:0">
            <input type="text" id="c-fat" inputmode="numeric" value="500.000" data-calc-fat
                   aria-describedby="c-fat-hint">
          </div>
          <small id="c-fat-hint" style="display:block;font-size:.78rem;color:var(--tx-3);margin-top:8px">
            Considere só o que depende de estar conectado — vendas, atendimento, produção.
          </small>
        </div>

        <div class="calc__field">
          <label class="calc__label" for="c-horas">
            <span>Horas de operação por mês</span>
          </label>
          <div class="calc__chips" role="group" aria-label="Regime de operação">
            <button type="button" class="calc__chip" data-calc-regime="176" aria-pressed="true">Comercial · 176h</button>
            <button type="button" class="calc__chip" data-calc-regime="264" aria-pressed="false">Estendido · 264h</button>
            <button type="button" class="calc__chip" data-calc-regime="720" aria-pressed="false">24/7 · 720h</button>
          </div>
        </div>

        <div class="calc__field">
          <label class="calc__label" for="c-parada">
            <span>Horas paradas por mês</span>
            <small class="calc__val" data-calc-parada-val>2h</small>
          </label>
          <input type="range" class="dim__range" id="c-parada" min="0.5" max="16" step="0.5" value="2"
                 data-calc-parada>
          <div class="dim__scale"><span>30 min</span><span>4h</span><span>8h</span><span>16h</span></div>
          <small style="display:block;font-size:.78rem;color:var(--tx-3);margin-top:10px">
            Some quedas de link, instabilidade e manutenção não programada.
          </small>
        </div>

        <div class="calc__field">
          <label class="calc__label" for="c-unid">
            <span>Unidades afetadas</span>
            <small class="calc__val" data-calc-unid-val>1</small>
          </label>
          <input type="range" class="dim__range" id="c-unid" min="1" max="40" step="1" value="1"
                 data-calc-unid>
          <div class="dim__scale"><span>1</span><span>10</span><span>25</span><span>40</span></div>
          <small style="display:block;font-size:.78rem;color:var(--tx-3);margin-top:10px">
            Matriz, filiais ou pontos de venda que param junto quando o link cai.
          </small>
        </div>

      </div>

      <aside class="calc__out" aria-live="polite">
        <div class="calc__out-head">
          <b>Resultado</b>
          <span>Estimativa com base nos números que você informou</span>
        </div>
        <div class="calc__out-body">

          <div class="calc__hero-num" data-calc-ano>R$ 0</div>
          <div class="calc__hero-lbl">de faturamento perdido por ano</div>

          <div class="calc__rows">
            <div class="calc__row">
              <span>Faturamento por hora</span>
              <b data-calc-hora>R$ 0</b>
            </div>
            <div class="calc__row">
              <span>Custo de cada hora parada</span>
              <b data-calc-hora-total>R$ 0</b>
            </div>
            <div class="calc__row calc__row--total">
              <span>Perda estimada por mês</span>
              <b data-calc-mes>R$ 0</b>
            </div>
          </div>

          <div class="calc__note">
            Esta conta considera apenas o faturamento perdido. Não entram: hora de equipe
            parada, retrabalho da TI, multa contratual, cliente que desistiu e não voltou,
            nem o custo do chamado com a operadora.
            <strong>O prejuízo real costuma ser maior.</strong>
          </div>

          <div class="calc__actions">
            <a href="solucoes/link-dedicado-empresarial.html#form" class="btn btn--primary btn--wide">
              Solicitar avaliação da minha rede {ARROW}
            </a>
            <a href="solucoes/link-dedicado-empresarial.html#failover" class="btn btn--ghost btn--wide">
              Ver como o backup automático funciona
            </a>
          </div>

        </div>
      </aside>

    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">O que a conta não mostra</span>
      <h2 class="display">O prejuízo de uma queda não para no faturamento</h2>
      <p class="lead">
        A calculadora acima é deliberadamente conservadora. Estes custos são reais,
        mas difíceis de estimar sem conhecer sua operação.
      </p>
    </div>

    <div class="grid grid--3">
      <div class="pain reveal">
        <div class="pain__ico">{ico(I_TEAM, 21)}</div>
        <div>
          <h3>Equipe parada, salário correndo</h3>
          <p>Vinte pessoas sem sistema por duas horas são quarenta horas de trabalho pagas e não entregues.</p>
        </div>
      </div>
      <div class="pain reveal" data-d="1">
        <div class="pain__ico">{ico('<path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/>', 21)}</div>
        <div>
          <h3>Cliente que desiste e não volta</h3>
          <p>Quem ligou e não foi atendido, ou chegou na loja e não conseguiu pagar, raramente tenta de novo.</p>
        </div>
      </div>
      <div class="pain reveal" data-d="2">
        <div class="pain__ico">{ico('<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>', 21)}</div>
        <div>
          <h3>O tempo da TI apagando incêndio</h3>
          <p>Abrir chamado, cobrar a operadora, explicar para a diretoria. Horas que sairiam de projeto estratégico.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <span class="eyebrow">O outro lado da conta</span>
        <h2 class="display" style="margin-bottom:20px">Redundância é seguro: só parece cara antes de precisar</h2>
        <p class="lead" style="margin-bottom:22px">
          Compare o número que apareceu acima com o custo mensal de uma camada de
          contingência. Na maioria das operações, <strong>uma única ocorrência evitada
          paga o ano inteiro</strong>.
        </p>
        <p class="lead muted">
          Não colocamos preço nesta página de propósito: cada operação tem uma
          arquitetura diferente, e um valor genérico aqui não ajudaria você a decidir nada.
          A proposta sai depois que entendemos sua estrutura.
        </p>
      </div>
      <div class="callout">
        <h3>Como reduzimos essas horas</h3>
        <p>O Link.Box monitora a conexão principal e, quando ela falha, migra o tráfego
        para dois chips 4G/5G de operadoras diferentes — em pouco mais de um segundo,
        sem ninguém precisar agir.</p>
        <p>As horas paradas que você somou lá em cima deixam de existir na maior parte
        dos casos. O usuário final nem percebe que houve troca.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt section--tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <div class="cta-band__inner">
        <div>
          <h2 class="display">Vamos olhar onde sua rede está vulnerável</h2>
          <p class="lead">
            Avaliamos sua estrutura atual e mostramos onde existe ponto único de falha.
            Sem compromisso.
          </p>
        </div>
        <div class="cta-band__actions">
          <a href="solucoes/link-dedicado-empresarial.html#form" class="btn btn--primary btn--wide">Solicitar avaliação {ARROW}</a>
          <a href="tel:{TEL_HREF}" class="btn btn--ghost btn--wide">Ligar: {TEL}</a>
        </div>
      </div>
    </div>
  </div>
</section>
</main>
"""
