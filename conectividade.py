#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Páginas de conectividade — Link Dedicado e Link.Box.

São DUAS soluções diferentes e cada uma tem página própria:

  Link Dedicado  → a conexão em si. Fibra ou rádio, banda garantida
                   e simétrica, IP fixo, SLA.

  Link.Box       → o equipamento proprietário que gerencia múltiplos links
                   e faz a comutação automática para dois chips 4G/5G.
                   Funciona SOBRE um link que já existe, inclusive de
                   outra operadora.

Dá para contratar uma sem a outra. Juntas formam a oferta completa,
e por isso cada página aponta para a outra.
"""

from sections import ico, foto, FAILOVER, MOCK_NOC, mockup_section

P = "../"
WPP_HREF = "551131817756"
TEL, TEL_HREF = "(11) 4800-5000", "+551148005000"

CHECK = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<polyline points="20 6 9 17 4 12"/></svg>')
ARROW = ico('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>', 17, 2.5)


def checklist(itens):
    li = "".join(f"<li>{CHECK}<span>{i}</span></li>" for i in itens)
    return f'<ul class="checklist">{li}</ul>'


# ===========================================================================
# LINK DEDICADO — a conexão
# ===========================================================================
FAQ_DEDICADO = [
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
     "disponibilidade mensal. É o que separa um contrato empresarial de um plano residencial — "
     "e é por isso que atuamos só onde conseguimos cumprir o prazo."),
    ("Em quanto tempo o link é ativado?",
     "Depende da viabilidade técnica no endereço. Onde já existe fibra instalada, a ativação "
     "costuma ocorrer em poucos dias. Em rádio, geralmente é mais rápido. A consulta de "
     "disponibilidade responde isso antes de qualquer proposta."),
]

BODY_DEDICADO = f"""
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        <nav class="crumb" aria-label="Você está em">
          <a href="{P}index.html">Início</a>
          {ico('<polyline points="9 18 15 12 9 6"/>', 12, 2.5)}
          <a href="{P}index.html#solucoes">Soluções</a>
          {ico('<polyline points="9 18 15 12 9 6"/>', 12, 2.5)}
          <span>Link dedicado</span>
        </nav>
        <span class="eyebrow">Conectividade empresarial</span>
        <h1 class="display">Link dedicado empresarial com <span class="grad-text">banda garantida e IP fixo</span></h1>
        <p class="lead">
          A conexão que sua operação usa para trabalhar não pode ser a mesma que a de uma casa.
          Banda simétrica, IP fixo, SLA em contrato e monitoramento 24/7 — em fibra ou rádio.
        </p>
        <div class="hero__actions">
          <a href="#form" class="btn btn--primary">Consultar disponibilidade no meu endereço {ARROW}</a>
          <a href="https://wa.me/{WPP_HREF}" data-pos="hero-dedicado" class="btn btn--ghost" target="_blank" rel="noopener">Falar com um especialista</a>
        </div>
        <div class="hero__seals">
          <div class="seal">{CHECK} Banda garantida e simétrica</div>
          <div class="seal">{CHECK} IP fixo incluso</div>
          <div class="seal">{CHECK} SLA contratual</div>
        </div>
      </div>
      {{FORM_DEDICADO}}
    </div>
  </div>
</section>

{{PROOF}}

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">A diferença que aparece na conta</span>
      <h2 class="display">Banda larga comum × Link dedicado</h2>
      <p class="lead">
        A velocidade contratada é a parte menos importante da comparação.
        O que muda é o que você recebe quando a rede fica cheia.
      </p>
    </div>
    <div class="table-scroll reveal">
      <table class="compare">
        <thead><tr><th></th><th>Banda larga comum</th><th>Link dedicado Wicorp</th></tr></thead>
        <tbody>
          <tr><td>Banda contratada</td><td class="no">Velocidade máxima, compartilhada</td><td class="yes">Garantida e exclusiva</td></tr>
          <tr><td>Upload</td><td class="no">Muito menor que o download</td><td class="yes">Simétrico</td></tr>
          <tr><td>Comportamento no pico</td><td class="no">Cai quando o bairro usa</td><td class="yes">Não muda</td></tr>
          <tr><td>IP</td><td class="no">Dinâmico</td><td class="yes">Fixo</td></tr>
          <tr><td>SLA</td><td class="no">Não existe</td><td class="yes">Prazo em contrato</td></tr>
          <tr><td>Suporte</td><td class="no">Central de atendimento residencial</td><td class="yes">Equipe técnica própria</td></tr>
          <tr><td>Monitoramento</td><td class="no">Nenhum</td><td class="yes">NOC 24/7</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <span class="eyebrow">Fibra ou rádio</span>
        <h2 class="display" style="margin-bottom:20px">Duas formas de chegar até você</h2>
        <p class="lead" style="margin-bottom:26px">
          A escolha não é de gosto: depende do que existe no seu endereço.
          A consulta de disponibilidade responde antes de qualquer proposta.
        </p>
        <h3 style="font-size:1.05rem;margin-bottom:10px">Fibra óptica</h3>
        <p style="font-size:.94rem;color:var(--tx-2);line-height:1.7;margin-bottom:22px">
          Primeira opção quando há infraestrutura no local. Maior capacidade, menor latência
          e mais estabilidade. Exige que a fibra chegue até o endereço.
        </p>
        <h3 style="font-size:1.05rem;margin-bottom:10px">Rádio</h3>
        <p style="font-size:.94rem;color:var(--tx-2);line-height:1.7">
          Resolve onde a fibra não chegou ou onde a obra civil inviabiliza a instalação.
          A ativação costuma ser mais rápida e não depende de passagem de cabo na rua.
        </p>
      </div>
      <div>
        <span class="eyebrow">O que vem junto</span>
        {checklist([
          "Banda garantida e simétrica, sem compartilhamento",
          "IP fixo para publicar serviços e usar VPN",
          "SLA com prazo de atendimento definido em contrato",
          "Monitoramento proativo 24/7 pelo nosso NOC",
          "Suporte técnico próprio, sem fila de operadora",
          "Instalação e ativação com equipe em campo",
        ])}
      </div>
    </div>
  </div>
</section>

{{MOCK_NOC}}

<section class="section section--alt">
  <div class="wrap">
    <div class="split reveal">
      <div class="callout">
        <h3>Link dedicado não é o mesmo que redundância</h3>
        <p>Um link dedicado bem dimensionado é estável — mas continua sendo <strong>um único
        caminho</strong>. Se a fibra romper na rua ou a operadora fizer manutenção, ele cai como
        qualquer outro.</p>
        <p>Quem não pode parar precisa de uma segunda rota, independente da primeira.
        É exatamente para isso que existe o Link.Box.</p>
      </div>
      <div>
        <span class="eyebrow">O passo seguinte</span>
        <h2 class="display" style="margin-bottom:18px">E se este link cair?</h2>
        <p class="lead" style="margin-bottom:24px">
          O Link.Box é o equipamento que monitora sua conexão principal e, quando ela falha,
          migra o tráfego para dois chips 4G/5G de operadoras diferentes — sem ninguém precisar agir.
        </p>
        <a href="link-box-redundancia.html" class="btn btn--primary">Conhecer o Link.Box {ARROW}</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Perguntas frequentes</span>
      <h2 class="display">Dúvidas de quem está avaliando</h2>
    </div>
    <div class="reveal">{{FAQ_DEDICADO}}</div>
  </div>
</section>

{{CTA_DEDICADO}}
</main>
"""


# ===========================================================================
# LINK.BOX — o equipamento de redundância
# ===========================================================================
FAQ_LINKBOX = [
    ("O Link.Box funciona com o link que eu já tenho?",
     "Sim — e é assim que a maioria dos clientes começa. O Link.Box trabalha sobre a conexão que "
     "já existe no local, inclusive se ela for de outra operadora. Você não precisa trocar de "
     "fornecedor de internet para ter redundância."),
    ("Preciso contratar link dedicado da Wicorp junto?",
     "Não. São duas soluções independentes. Muitas empresas mantêm o link atual e adicionam "
     "apenas a camada de redundância. Contratar as duas com a gente simplifica o suporte, porque "
     "passa a existir um único responsável pela conexão inteira — mas não é obrigatório."),
    ("Quanto tempo leva a comutação?",
     "Pouco mais de um segundo na maior parte dos casos. O equipamento confirma a falha em três "
     "tentativas antes de comutar, para não trocar de rota por causa de uma oscilação passageira. "
     "Quando o link principal volta, o tráfego é devolvido automaticamente."),
    ("Por que dois chips, e de operadoras diferentes?",
     "Porque redundância exige caminhos independentes. Dois chips da mesma operadora caem juntos "
     "quando a torre da região tem problema. Com operadoras distintas, a chance de as duas falharem "
     "ao mesmo tempo é muito menor."),
    ("Alguém da minha equipe precisa fazer algo quando o link cai?",
     "Não. A comutação é automática e o NOC recebe o alerta. Na maioria dos casos o usuário final "
     "nem percebe que houve troca de rota — o que muda é que ninguém abre chamado às pressas."),
    ("Serve para operação com várias unidades?",
     "É justamente onde faz mais diferença. Redes de varejo, farmácias e operações distribuídas "
     "usam o Link.Box para que uma unidade isolada não pare por falha de uma única operadora."),
]

BODY_LINKBOX = f"""
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        <nav class="crumb" aria-label="Você está em">
          <a href="{P}index.html">Início</a>
          {ico('<polyline points="9 18 15 12 9 6"/>', 12, 2.5)}
          <a href="{P}index.html#solucoes">Soluções</a>
          {ico('<polyline points="9 18 15 12 9 6"/>', 12, 2.5)}
          <span>Link.Box</span>
        </nav>
        <span class="eyebrow">Tecnologia proprietária Wicorp</span>
        <h1 class="display">Link.Box: redundância de internet com <span class="grad-text">dois chips 4G/5G</span></h1>
        <p class="lead">
          O equipamento que mantém sua operação online quando a conexão principal cai.
          Funciona sobre o link que você já tem — inclusive de outra operadora.
        </p>
        <div class="hero__actions">
          <a href="#form" class="btn btn--primary">Simular uma arquitetura de redundância {ARROW}</a>
          <a href="#failover" class="btn btn--ghost">Ver a comutação acontecer</a>
        </div>
        <div class="hero__seals">
          <div class="seal">{CHECK} Comutação automática</div>
          <div class="seal">{CHECK} Duas operadoras diferentes</div>
          <div class="seal">{CHECK} +700 em operação</div>
        </div>
      </div>
      {{FORM_LINKBOX}}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="split reveal">
      <div class="foto-produto">
        {foto("link-box", "Link.Box 5G da Wicorp, equipamento preto com quatro antenas e faixa azul-turquesa com a marca",
              ratio="4/3", ext="png", prefix=P, larguras=(700, 1200), loading="eager", radius="0")}
      </div>
      <div>
        <span class="eyebrow">O equipamento</span>
        <h2 class="display" style="margin-bottom:20px">Não é software. É um aparelho no seu rack.</h2>
        <p class="lead" style="margin-bottom:22px">
          O Link.Box fica instalado na sua operação, entre o link e a rede interna.
          Ele monitora a conexão principal continuamente e assume o controle quando ela falha.
        </p>
        {checklist([
          "Duas portas LAN e uma porta de internet para o link existente",
          "Dois chips 4G/5G de operadoras distintas, já embarcados",
          "Quatro antenas para captação de sinal móvel",
          "Alimentação por PoE ou fonte, com porta serial para configuração",
          "Monitorado remotamente pelo nosso NOC, 24 horas por dia",
        ])}
      </div>
    </div>
  </div>
</section>

{{FAILOVER}}

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Por que dois links não bastam</span>
      <h2 class="display">Redundância exige caminhos independentes</h2>
      <p class="lead">
        Contratar um segundo link ajuda menos do que parece — e este é o comparativo
        que costuma decidir a conversa.
      </p>
    </div>
    <div class="table-scroll reveal">
      <table class="compare">
        <thead><tr><th>Cenário</th><th>Link único</th><th>Dois links, mesma operadora</th><th>Link.Box</th></tr></thead>
        <tbody>
          <tr><td>Rompimento de fibra na rua</td><td class="no">Operação para</td><td class="no">Ambos caem juntos</td><td class="yes">Comuta para o 5G</td></tr>
          <tr><td>Manutenção da operadora</td><td class="no">Operação para</td><td class="no">Ambos afetados</td><td class="yes">Segue online</td></tr>
          <tr><td>Tempo de indisponibilidade</td><td>Horas, até o reparo</td><td>Horas, se a falha for na operadora</td><td class="yes">Cerca de 1 segundo</td></tr>
          <tr><td>Ação necessária da equipe</td><td>Abrir chamado e aguardar</td><td>Trocar manualmente</td><td class="yes">Nenhuma</td></tr>
          <tr><td>Dependência de fornecedor único</td><td class="no">Total</td><td class="no">Total</td><td class="yes">Nenhuma</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <span class="eyebrow">Onde faz mais diferença</span>
        <h2 class="display" style="margin-bottom:22px">Operações que não podem esperar o reparo</h2>
        {checklist([
          "Redes de varejo e farmácias — um PDV sem conexão não emite fiscal nem processa pagamento",
          "Operações com várias filiais — a unidade isolada perde sistema, telefonia e contato com a matriz",
          "Indústrias — sistemas de produção e apontamento param junto",
          "Operações de atendimento — telefonia em nuvem cai junto com a internet",
          "Empresas com ERP em nuvem — sem link, não há sistema",
        ])}
        <a href="{P}calculadora-custo-downtime.html" class="btn btn--ghost" style="margin-top:26px">
          Calcular quanto uma hora parada custa {ARROW}
        </a>
      </div>
      <div>
        <div class="foto-frame">
          {foto("link-box-mesa", "Link.Box 5G instalado sobre uma bancada no escritório da Wicorp",
                ratio="4/3", prefix=P, larguras=(600, 600))}
        </div>
        <p class="foto-cap">
          São mais de 700 equipamentos em operação em redes de varejo, indústrias
          e instituições de ensino.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <span class="eyebrow">E a conexão principal?</span>
        <h2 class="display" style="margin-bottom:18px">O Link.Box protege o link. Não substitui ele.</h2>
        <p class="lead" style="margin-bottom:24px">
          A redundância entra em ação quando algo falha. No dia a dia, quem sustenta a operação
          é a conexão principal — e ela precisa ter banda garantida, IP fixo e SLA.
        </p>
        <a href="link-dedicado-empresarial.html" class="btn btn--primary">Conhecer o link dedicado {ARROW}</a>
      </div>
      <div class="callout">
        <h3>Dá para contratar só a redundância</h3>
        <p>Muitos clientes começam mantendo o link que já têm — de qualquer operadora — e
        adicionam apenas o Link.Box. Funciona, e é o caminho mais rápido para eliminar
        o ponto único de falha.</p>
        <p>Contratar as duas coisas conosco simplifica o suporte: passa a existir um único
        responsável pela conexão inteira, em vez de dois fornecedores apontando um para o outro.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Perguntas frequentes</span>
      <h2 class="display">Dúvidas de quem está avaliando</h2>
    </div>
    <div class="reveal">{{FAQ_LINKBOX}}</div>
  </div>
</section>

{{CTA_LINKBOX}}
</main>
"""
