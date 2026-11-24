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
WPP_HREF = "551150287515"
TEL, TEL_HREF = "(11) 5028-7515", "+551150287515"

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
# ===========================================================================
# LINK DEDICADO — movido para produtos.py
#
# A pagina de link dedicado agora e gerada por produtos.py, nas duas versoes
# (solucao e landing page). O corpo antigo foi REMOVIDO daqui de proposito:
# ele afirmava monitoramento 24/7 pelo NOC e suporte proprio no link, o que
# NAO e verdade — a Wicorp representa o produto, quem da suporte e a operadora.
# Codigo morto com afirmacao errada volta a circular. Por isso saiu.
# ===========================================================================

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
          <div class="seal">{CHECK} +2.000 em operação</div>
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
          São mais de 2.000 equipamentos em operação em redes de varejo, indústrias
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
