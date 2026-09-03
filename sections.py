#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seções visuais e interativas da home.

Os mockups são interfaces reconstruídas em HTML/CSS dentro de uma moldura
de tela. Não usam banco de imagens: mostram o próprio ecossistema Wicorp,
que é o que o diagnóstico de criativos apontou como ausente.
"""

WPP_HREF = "551131817756"


def ico(path, size=18, sw=2.1):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{path}</svg>')


I_WIFI   = '<path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/>'
I_PHONE  = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>'
I_SHIELD = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'
I_SERVER = '<rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/>'
I_SIM    = '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M9 8h6v5H9z"/>'
I_FIBER  = '<path d="M4 12h4l3-8 4 16 3-8h2"/>'


# ===========================================================================
# 1. SIMULADOR DE FAILOVER — a peça interativa principal
#    Vem da recomendação de b-roll de failover em tempo real do plano.
# ===========================================================================
FAILOVER = f"""
<section class="section" id="failover">
  <div class="wrap">
    <div class="fail">

      <div class="reveal">
        <span class="eyebrow">Link.Box · tecnologia proprietária</span>
        <h2 class="display" style="margin-bottom:18px">Veja o que acontece quando a fibra cai</h2>
        <p class="lead" style="margin-bottom:22px">
          Este é o teste que fazemos em campo antes de entregar qualquer projeto.
          Derrube a conexão principal e acompanhe a comutação para os dois chips 4G/5G —
          sem ninguém precisar agir.
        </p>

        <div style="display:flex; gap:12px; flex-wrap:wrap; margin-bottom:24px">
          <button class="btn btn--primary" data-fail-trigger>
            <span data-fail-label>Simular queda do link</span>
            {ico('<polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/>', 17, 2.4)}
          </button>
          <button class="btn btn--ghost" data-fail-reset disabled>Restaurar</button>
        </div>

        <p class="muted" style="font-size:.84rem">
          Demonstração fiel ao comportamento real do equipamento. Em campo, a comutação
          é validada com teste presencial antes da entrega.
        </p>
      </div>

      <div class="fail__stage reveal" data-d="1">
        <div class="screen">
          <div class="screen__bar">
            <span class="screen__dot"></span><span class="screen__dot"></span><span class="screen__dot"></span>
            <span class="screen__title">Link.Box · Matriz São Paulo</span>
            <span class="screen__live">Ao vivo</span>
          </div>
          <div class="screen__body">

            <div class="route is-active" data-route="fibra">
              <div class="route__ico">{ico(I_FIBER, 19)}</div>
              <div class="route__info">
                <div class="route__name">Fibra dedicada · 300 Mbps</div>
                <div class="route__meta" data-route-meta>Latência 8 ms · perda 0,0%</div>
                <div class="route__flow"></div>
              </div>
              <span class="route__state" data-route-state>Ativo</span>
            </div>

            <div class="route is-standby" data-route="sim1">
              <div class="route__ico">{ico(I_SIM, 19)}</div>
              <div class="route__info">
                <div class="route__name">Backup 5G · Operadora A</div>
                <div class="route__meta" data-route-meta>Em espera · sinal −67 dBm</div>
                <div class="route__flow"></div>
              </div>
              <span class="route__state" data-route-state>Standby</span>
            </div>

            <div class="route is-standby" data-route="sim2">
              <div class="route__ico">{ico(I_SIM, 19)}</div>
              <div class="route__info">
                <div class="route__name">Backup 4G · Operadora B</div>
                <div class="route__meta" data-route-meta>Em espera · sinal −72 dBm</div>
                <div class="route__flow"></div>
              </div>
              <span class="route__state" data-route-state>Standby</span>
            </div>

            <div class="fail__status">
              <span class="fail__badge" data-fail-badge>
                {ico('<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>', 15, 2.4)}
                <span data-fail-badge-txt>Operação conectada</span>
              </span>
              <div class="fail__timer">
                <span data-fail-uptime>99,98%</span>
                <small data-fail-uptime-lbl>disponibilidade no mês</small>
              </div>
            </div>

            <div class="fail__log" data-fail-log>
              <span>NOC · monitoramento ativo em 3 rotas</span>
            </div>

          </div>
        </div>
      </div>

    </div>
  </div>
</section>
"""


# ===========================================================================
# 2. MOCKUPS DE INTERFACE — um por solução
# ===========================================================================
MOCK_NOC = f"""
<div class="screen">
  <div class="screen__bar">
    <span class="screen__dot"></span><span class="screen__dot"></span><span class="screen__dot"></span>
    <span class="screen__title">NOC Wicorp · monitoramento de links</span>
    <span class="screen__live">24/7</span>
  </div>
  <div class="screen__body">
    <div class="ui">
      <div class="ui__grid ui__grid--3" style="margin-bottom:18px">
        <div class="ui__kpi ui__kpi--ok"><b>99,98%</b><span>Disponibilidade</span></div>
        <div class="ui__kpi ui__kpi--info"><b>8 ms</b><span>Latência média</span></div>
        <div class="ui__kpi ui__kpi--warn"><b>2</b><span>Alertas hoje</span></div>
      </div>

      <div style="font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--tx-3);margin-bottom:8px">
        Latência · últimas 24h
      </div>
      <svg class="spark" viewBox="0 0 320 78" preserveAspectRatio="none" role="img" aria-label="Gráfico de latência estável nas últimas 24 horas">
        <defs>
          <linearGradient id="sparkgrad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#5BBFC6"/><stop offset="100%" stop-color="#C7D86E"/>
          </linearGradient>
          <linearGradient id="sparkfill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#74BE9A" stop-opacity=".28"/>
            <stop offset="100%" stop-color="#74BE9A" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <path class="area" d="M0,54 L26,50 L52,56 L78,44 L104,48 L130,38 L156,46 L182,34 L208,42 L234,30 L260,40 L286,32 L320,36 L320,78 L0,78 Z"/>
        <path class="line" d="M0,54 L26,50 L52,56 L78,44 L104,48 L130,38 L156,46 L182,34 L208,42 L234,30 L260,40 L286,32 L320,36"/>
      </svg>

      <div style="margin-top:14px">
        <div class="ui__row">
          <div class="ui__av">SP</div>
          <div><div class="ui__label">Matriz · São Paulo</div><div class="ui__sub">Fibra 300 Mbps + backup 5G</div></div>
          <span class="ui__tag ui__tag--ok ui__spacer">Online</span>
        </div>
        <div class="ui__row">
          <div class="ui__av">GU</div>
          <div><div class="ui__label">Filial · Guarulhos</div><div class="ui__sub">Fibra 200 Mbps + backup 4G</div></div>
          <span class="ui__tag ui__tag--ok ui__spacer">Online</span>
        </div>
        <div class="ui__row">
          <div class="ui__av ui__av--mut">OS</div>
          <div><div class="ui__label">Loja · Osasco</div><div class="ui__sub">Comutado para backup há 2 min</div></div>
          <span class="ui__tag ui__tag--warn ui__spacer">Em backup</span>
        </div>
      </div>
    </div>
  </div>
</div>
"""

MOCK_PABX = f"""
<div class="screen">
  <div class="screen__bar">
    <span class="screen__dot"></span><span class="screen__dot"></span><span class="screen__dot"></span>
    <span class="screen__title">wcloud · painel de atendimento</span>
    <span class="screen__live">12 em linha</span>
  </div>
  <div class="screen__body">
    <div class="ui">
      <div class="ui__grid ui__grid--3" style="margin-bottom:18px">
        <div class="ui__kpi ui__kpi--info"><b>12</b><span>Em atendimento</span></div>
        <div class="ui__kpi ui__kpi--warn"><b>0:42</b><span>Espera média</span></div>
        <div class="ui__kpi ui__kpi--ok"><b>97%</b><span>Atendidas hoje</span></div>
      </div>

      <div style="font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--tx-3);margin-bottom:4px">
        Fila ativa
      </div>
      <div class="ui__row">
        <div class="ui__av">RS</div>
        <div><div class="ui__label">Renata Souza · Comercial</div><div class="ui__sub">Ligação · 04:12</div></div>
        <span class="ui__tag ui__tag--ok ui__spacer">Em chamada</span>
      </div>
      <div class="ui__row">
        <div class="ui__av">MC</div>
        <div><div class="ui__label">Marcos Cunha · Suporte</div><div class="ui__sub">WhatsApp · 2 conversas</div></div>
        <span class="ui__tag ui__tag--ok ui__spacer">Disponível</span>
      </div>
      <div class="ui__row">
        <div class="ui__av ui__av--mut">AL</div>
        <div><div class="ui__label">Ana Lima · Financeiro</div><div class="ui__sub">Aguardando · 00:18</div></div>
        <span class="ui__tag ui__tag--warn ui__spacer">Na fila</span>
      </div>

      <div style="margin-top:16px;padding-top:14px;border-top:1px solid var(--line);display:flex;gap:9px;flex-wrap:wrap">
        <span class="ui__tag ui__tag--mut">{ico(I_PHONE, 12, 2.4)} Ligações</span>
        <span class="ui__tag ui__tag--mut">WhatsApp</span>
        <span class="ui__tag ui__tag--mut">Chat</span>
        <span class="ui__tag ui__tag--mut">E-mail</span>
        <span class="ui__tag ui__tag--ok">URA com IA ativa</span>
      </div>
    </div>
  </div>
</div>
"""

MOCK_FW = f"""
<div class="screen">
  <div class="screen__bar">
    <span class="screen__dot"></span><span class="screen__dot"></span><span class="screen__dot"></span>
    <span class="screen__title">Firewall gerenciado · visibilidade de rede</span>
    <span class="screen__live">Protegido</span>
  </div>
  <div class="screen__body">
    <div class="ui">
      <div class="ui__grid ui__grid--3" style="margin-bottom:18px">
        <div class="ui__kpi ui__kpi--ok"><b>1.284</b><span>Ameaças bloqueadas</span></div>
        <div class="ui__kpi ui__kpi--info"><b>142</b><span>Dispositivos</span></div>
        <div class="ui__kpi ui__kpi--warn"><b>3</b><span>Políticas a revisar</span></div>
      </div>

      <div style="font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--tx-3);margin-bottom:10px">
        Consumo por aplicação
      </div>
      <div style="margin-bottom:11px">
        <div style="display:flex;justify-content:space-between;font-size:.8rem">
          <span class="ui__label">Sistema ERP</span><span class="ui__sub">38%</span>
        </div>
        <div class="ui__bar"><i style="width:38%"></i></div>
      </div>
      <div style="margin-bottom:11px">
        <div style="display:flex;justify-content:space-between;font-size:.8rem">
          <span class="ui__label">Videoconferência</span><span class="ui__sub">24%</span>
        </div>
        <div class="ui__bar"><i style="width:24%"></i></div>
      </div>
      <div style="margin-bottom:11px">
        <div style="display:flex;justify-content:space-between;font-size:.8rem">
          <span class="ui__label">Streaming não corporativo</span><span class="ui__sub">21%</span>
        </div>
        <div class="ui__bar ui__bar--warn"><i style="width:21%"></i></div>
      </div>
      <div>
        <div style="display:flex;justify-content:space-between;font-size:.8rem">
          <span class="ui__label">Destino bloqueado</span><span class="ui__sub">4%</span>
        </div>
        <div class="ui__bar ui__bar--err"><i style="width:4%"></i></div>
      </div>

      <div style="margin-top:16px;padding-top:14px;border-top:1px solid var(--line)">
        <div class="ui__row" style="padding:8px 0">
          <span class="ui__tag ui__tag--err">Bloqueado</span>
          <div class="ui__sub">Tentativa de conexão com destino malicioso · 14:02</div>
        </div>
        <div class="ui__row" style="padding:8px 0">
          <span class="ui__tag ui__tag--warn">Alerta</span>
          <div class="ui__sub">Acesso fora do horário · estação RH-14 · 03:47</div>
        </div>
      </div>
    </div>
  </div>
</div>
"""

MOCK_INFRA = f"""
<div class="screen">
  <div class="screen__bar">
    <span class="screen__dot"></span><span class="screen__dot"></span><span class="screen__dot"></span>
    <span class="screen__title">Topologia · unidade mapeada</span>
    <span class="screen__live">Documentado</span>
  </div>
  <div class="screen__body">
    <svg viewBox="0 0 460 250" style="width:100%;height:auto" role="img"
         aria-label="Diagrama da topologia de rede: link chega ao rack e distribui para switches, pontos de Wi-Fi e câmeras">
      <defs>
        <linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="#5BBFC6"/><stop offset="100%" stop-color="#C7D86E"/>
        </linearGradient>
      </defs>

      <!-- ligacoes -->
      <g stroke="rgba(255,255,255,.16)" stroke-width="1.6" fill="none">
        <path d="M230 62 V96"/>
        <path d="M230 128 V150 H110 V172"/>
        <path d="M230 128 V150 H230 V172"/>
        <path d="M230 128 V150 H350 V172"/>
      </g>
      <g stroke="url(#tg)" stroke-width="1.6" fill="none" opacity=".55">
        <path d="M230 62 V96"><animate attributeName="stroke-dasharray" values="0 40;40 0" dur="2.2s" repeatCount="indefinite"/></path>
      </g>

      <!-- link externo -->
      <rect x="168" y="30" width="124" height="32" rx="9" fill="rgba(91,191,198,.12)" stroke="rgba(91,191,198,.4)"/>
      <text x="230" y="50" text-anchor="middle" fill="#B9C6CC" font-family="Roboto,sans-serif" font-size="11.5">Link dedicado + backup</text>

      <!-- rack central -->
      <circle cx="230" cy="112" r="14" fill="none" stroke="#74BE9A" stroke-width="1.4" class="node-pulse" opacity=".35"/>
      <rect x="196" y="96" width="68" height="32" rx="9" fill="rgba(116,190,154,.16)" stroke="rgba(116,190,154,.5)"/>
      <text x="230" y="116" text-anchor="middle" fill="#fff" font-family="Roboto,sans-serif" font-size="11.5" font-weight="600">Rack</text>

      <!-- pontos finais -->
      <g font-family="Roboto,sans-serif" font-size="10.5" fill="#7C8C94" text-anchor="middle">
        <rect x="60" y="172" width="100" height="46" rx="9" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.12)"/>
        <text x="110" y="192" fill="#B9C6CC" font-size="11.5">Wi-Fi corporativo</text>
        <text x="110" y="207">14 pontos de acesso</text>

        <rect x="180" y="172" width="100" height="46" rx="9" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.12)"/>
        <text x="230" y="192" fill="#B9C6CC" font-size="11.5">Estações</text>
        <text x="230" y="207">142 dispositivos</text>

        <rect x="300" y="172" width="100" height="46" rx="9" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.12)"/>
        <text x="350" y="192" fill="#B9C6CC" font-size="11.5">CFTV</text>
        <text x="350" y="207">28 câmeras</text>
      </g>
    </svg>

    <div class="ui" style="margin-top:16px;padding-top:14px;border-top:1px solid var(--line)">
      <div class="ui__grid ui__grid--3">
        <div class="ui__kpi ui__kpi--ok"><b>100%</b><span>Pontos certificados</span></div>
        <div class="ui__kpi ui__kpi--info"><b>as-built</b><span>Projeto entregue</span></div>
        <div class="ui__kpi ui__kpi--info"><b>SLA 4h</b><span>Atendimento</span></div>
      </div>
    </div>
  </div>
</div>
"""


# ===========================================================================
# 3. ABAS DE SOLUÇÃO
# ===========================================================================
TABS = f"""
<section class="section section--alt" id="solucoes">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Ecossistema Wicorp</span>
      <h2 class="display">Quatro frentes, um único parceiro</h2>
      <p class="lead">
        Conectividade, comunicação, segurança e infraestrutura desenhadas em conjunto —
        com uma equipe que enxerga sua operação inteira, não um pedaço dela.
      </p>
    </div>

    <div class="tabs reveal">
      <div class="tabs__nav" role="tablist" aria-label="Soluções Wicorp">

        <button class="tab" role="tab" aria-selected="true" aria-controls="p-noc" id="t-noc" data-tab="noc">
          <span class="tab__ico">{ico(I_WIFI, 20)}</span>
          <span class="tab__txt"><b>Link dedicado e Link.Box</b><span>Conexão com backup automático 4G/5G</span></span>
        </button>

        <button class="tab" role="tab" aria-selected="false" aria-controls="p-pabx" id="t-pabx" data-tab="pabx" tabindex="-1">
          <span class="tab__ico">{ico(I_PHONE, 20)}</span>
          <span class="tab__txt"><b>PABX virtual com IA</b><span>Telefonia e atendimento em nuvem</span></span>
        </button>

        <button class="tab" role="tab" aria-selected="false" aria-controls="p-fw" id="t-fw" data-tab="fw" tabindex="-1">
          <span class="tab__ico">{ico(I_SHIELD, 20)}</span>
          <span class="tab__txt"><b>Firewall e SD-WAN</b><span>Proteção de rede gerenciada</span></span>
        </button>

        <button class="tab" role="tab" aria-selected="false" aria-controls="p-infra" id="t-infra" data-tab="infra" tabindex="-1">
          <span class="tab__ico">{ico(I_SERVER, 20)}</span>
          <span class="tab__txt"><b>Infraestrutura e projetos</b><span>Cabeamento, Wi-Fi corporativo e CFTV</span></span>
        </button>

      </div>

      <div class="tabs__panels">

        <div class="panel is-on" id="p-noc" role="tabpanel" aria-labelledby="t-noc">
          {MOCK_NOC}
          <div class="panel__cap">
            <div class="panel__stat"><b>+700</b><span>equipamentos em campo</span></div>
            <div class="panel__stat"><b>4G/5G</b><span>backup em dois chips</span></div>
            <div class="panel__stat" style="margin-left:auto">
              <a href="solucoes/link-dedicado-empresarial.html" class="sol__cta">Conhecer link dedicado e Link.Box
                {ico('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>', 15, 2.5)}
              </a>
            </div>
          </div>
        </div>

        <div class="panel" id="p-pabx" role="tabpanel" aria-labelledby="t-pabx" hidden>
          {MOCK_PABX}
          <div class="panel__cap">
            <div class="panel__stat"><b>1 painel</b><span>ligações, WhatsApp e chat</span></div>
            <div class="panel__stat"><b>URA</b><span>com roteamento por assunto</span></div>
            <div class="panel__stat" style="margin-left:auto">
              <a href="solucoes/pabx-virtual-nuvem.html" class="sol__cta">Conhecer o PABX virtual com IA
                {ico('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>', 15, 2.5)}
              </a>
            </div>
          </div>
        </div>

        <div class="panel" id="p-fw" role="tabpanel" aria-labelledby="t-fw" hidden>
          {MOCK_FW}
          <div class="panel__cap">
            <div class="panel__stat"><b>24/7</b><span>monitoramento do NOC</span></div>
            <div class="panel__stat"><b>LGPD</b><span>registro para auditoria</span></div>
            <div class="panel__stat" style="margin-left:auto">
              <a href="solucoes/firewall-sd-wan.html" class="sol__cta">Conhecer firewall e SD-WAN
                {ico('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>', 15, 2.5)}
              </a>
            </div>
          </div>
        </div>

        <div class="panel" id="p-infra" role="tabpanel" aria-labelledby="t-infra" hidden>
          {MOCK_INFRA}
          <div class="panel__cap">
            <div class="panel__stat"><b>as-built</b><span>documentação na entrega</span></div>
            <div class="panel__stat"><b>Equipe própria</b><span>em campo</span></div>
            <div class="panel__stat" style="margin-left:auto">
              <a href="solucoes/infraestrutura-ti.html" class="sol__cta">Conhecer projetos de infraestrutura
                {ico('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>', 15, 2.5)}
              </a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>
"""


# ===========================================================================
# 4. FAIXA DE SETORES ATENDIDOS
# ===========================================================================
_SETORES = ["Redes de varejo", "Farmácias", "Indústrias", "Hospitais",
            "Instituições de ensino", "Logística e transporte",
            "Operações de atendimento", "Serviços empresariais",
            "Empresas com várias filiais"]

_CHECK = ico('<polyline points="20 6 9 17 4 12"/>', 17, 2.4)
_ITENS = "".join(f'<div class="marquee__item">{_CHECK}{s}</div>' for s in _SETORES)

MARQUEE = f"""
<section class="section--tight" style="padding:44px 0; border-block:1px solid var(--line)">
  <div class="wrap" style="margin-bottom:22px; text-align:center">
    <p class="muted" style="font-size:.82rem; letter-spacing:.1em; text-transform:uppercase">
      Operações que não podem parar — em São Paulo e Grande São Paulo
    </p>
  </div>
  <div class="marquee">
    <div class="marquee__track">{_ITENS}{_ITENS}</div>
  </div>
</section>
"""
