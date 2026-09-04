#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de páginas do site Wicorp.

Header, rodapé e <head> ficam definidos aqui uma única vez. Cada página
declara apenas o próprio conteúdo. Rodar este script escreve os arquivos
HTML estáticos finais — o site continua sendo HTML puro, sem dependência
de servidor.

    python3 build.py

O logo é referenciado como img/logo-wicorp.png em todas as páginas.
Para trocar a marca, basta substituir aquele arquivo.
"""
import pathlib
import sections
import paginas

ROOT = pathlib.Path(__file__).parent
SITE = "https://wicorp.com.br"

TEL, TEL_HREF = "(11) 4800-5000", "+551148005000"
WPP, WPP_HREF = "(11) 3181-7756", "551131817756"
MAIL = "comercial@wicorp.com.br"


# ---------------------------------------------------------------------------
# Partials
# ---------------------------------------------------------------------------
def head(title, desc, canonical, prefix):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{canonical}">
<meta name="robots" content="index, follow">

<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Wicorp">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#080C0E">

<link rel="icon" href="{prefix}img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Roboto:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body>
<a class="skip" href="#main">Ir para o conteúdo</a>
"""


def logo(prefix, cls=""):
    return (f'<a href="{prefix}index.html" class="logo {cls}" aria-label="Wicorp — página inicial">'
            f'<img src="{prefix}img/logo-wicorp.png" alt="Wicorp — Conexões Inteligentes" width="208" height="197">'
            f'</a>')


def header(prefix, active=""):
    def cls(name):
        return ' style="color:#fff"' if active == name else ""
    return f"""
<header class="header">
  <div class="wrap">
    {logo(prefix)}
    <nav class="nav" aria-label="Navegação principal">
      <div class="nav__item">
        <a href="{prefix}index.html#solucoes" class="nav__link"{cls('sol')}>
          Soluções
          <svg class="nav__caret" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        <div class="dropdown">
          <a href="{prefix}solucoes/link-dedicado-empresarial.html"><b>Link dedicado e Link.Box</b><span>Internet dedicada com backup automático 4G/5G</span></a>
          <a href="{prefix}solucoes/pabx-virtual-nuvem.html"><b>PABX virtual com IA</b><span>Telefonia em nuvem, SIP Trunk e Contact Center</span></a>
          <a href="{prefix}solucoes/firewall-sd-wan.html"><b>Firewall e SD-WAN</b><span>Proteção de rede gerenciada e monitorada</span></a>
          <a href="{prefix}solucoes/infraestrutura-ti.html"><b>Infraestrutura e projetos</b><span>Cabeamento, Wi-Fi corporativo, CFTV e suporte</span></a>
        </div>
      </div>
      <a href="{prefix}index.html#diferenciais" class="nav__link">Diferenciais</a>
      <a href="{prefix}quem-somos.html" class="nav__link">Quem somos</a>
      <a href="{prefix}blog/index.html" class="nav__link">Blog</a>
      <a href="{prefix}contato.html" class="nav__link"{cls('contato')}>Contato</a>
    </nav>
    <a href="{prefix}contato.html" class="btn btn--primary btn--sm header__cta">Falar com um especialista</a>
    <button class="burger" aria-label="Abrir menu" aria-expanded="false" aria-controls="mobile-menu"><span></span></button>
  </div>
</header>

<div class="mobile-menu" id="mobile-menu">
  <a href="{prefix}index.html#solucoes">Soluções</a>
  <a href="{prefix}solucoes/link-dedicado-empresarial.html" class="sub">Link dedicado e Link.Box</a>
  <a href="{prefix}solucoes/pabx-virtual-nuvem.html" class="sub">PABX virtual com IA</a>
  <a href="{prefix}solucoes/firewall-sd-wan.html" class="sub">Firewall e SD-WAN</a>
  <a href="{prefix}solucoes/infraestrutura-ti.html" class="sub">Infraestrutura e projetos</a>
  <a href="{prefix}index.html#diferenciais">Diferenciais</a>
  <a href="{prefix}quem-somos.html">Quem somos</a>
  <a href="{prefix}blog/index.html">Blog</a>
  <a href="{prefix}contato.html">Contato</a>
  <a href="{prefix}contato.html" class="btn btn--primary btn--wide">Falar com um especialista</a>
</div>
"""


def header_lp(prefix):
    """Header reduzido para landing page — sem menu, para não dar rota de fuga."""
    return f"""
<header class="header is-stuck">
  <div class="wrap">
    {logo(prefix)}
    <a href="tel:{TEL_HREF}" class="btn btn--ghost btn--sm" style="margin-left:auto">{TEL}</a>
  </div>
</header>
"""


def footer(prefix, lp=False):
    if lp:
        return f"""
<footer class="footer" style="padding-top:44px">
  <div class="wrap">
    <div class="footer__bar" style="border-top:none">
      <span>© 1998–<span data-year>2026</span> Wicorp — Conexões Inteligentes.</span>
      <span>{TEL} · {MAIL}</span>
    </div>
  </div>
</footer>
{wa(prefix)}
<script src="{prefix}js/main.js"></script>
</body>
</html>
"""
    return f"""
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        {logo(prefix)}
        <p>Desde 1998, entregando consultoria estratégica em Tecnologia da Informação e Comunicação.</p>
        <div class="social">
          <a href="https://www.instagram.com/wicorpconexoes/" target="_blank" rel="noopener" aria-label="Instagram da Wicorp"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
          <a href="https://www.linkedin.com/in/wicorp-conex%C3%B5es-inteligentes-480066185/" target="_blank" rel="noopener" aria-label="LinkedIn da Wicorp"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg></a>
          <a href="https://www.facebook.com/profile.php?id=100081075576327" target="_blank" rel="noopener" aria-label="Facebook da Wicorp"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
        </div>
      </div>
      <div>
        <h4>Soluções</h4>
        <ul>
          <li><a href="{prefix}solucoes/link-dedicado-empresarial.html">Link dedicado e Link.Box</a></li>
          <li><a href="{prefix}solucoes/pabx-virtual-nuvem.html">PABX virtual com IA</a></li>
          <li><a href="{prefix}solucoes/pabx-virtual-nuvem.html">SIP Trunk</a></li>
          <li><a href="{prefix}solucoes/pabx-virtual-nuvem.html">Contact Center</a></li>
          <li><a href="{prefix}solucoes/firewall-sd-wan.html">Firewall e SD-WAN</a></li>
          <li><a href="{prefix}solucoes/infraestrutura-ti.html">Wi-Fi corporativo e CFTV</a></li>
        </ul>
      </div>
      <div>
        <h4>Empresa</h4>
        <ul>
          <li><a href="{prefix}quem-somos.html">Quem somos</a></li>
          <li><a href="{prefix}index.html#diferenciais">Diferenciais</a></li>
          <li><a href="{prefix}blog/index.html">Blog</a></li>
          <li><a href="{prefix}calculadora-custo-downtime.html">Calculadora de downtime</a></li>
          <li><a href="{prefix}contato.html">Contato</a></li>
          <li><a href="https://wicorp.desk.ms" target="_blank" rel="noopener">Suporte ao cliente</a></li>
        </ul>
      </div>
      <div>
        <h4>Contato</h4>
        <ul class="footer__contact">
          <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg><a href="tel:{TEL_HREF}">{TEL}</a></li>
          <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8z"/></svg><a href="https://wa.me/{WPP_HREF}" data-pos="rodape" target="_blank" rel="noopener">{WPP}</a></li>
          <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22 6 12 13 2 6"/></svg><a href="mailto:{MAIL}">{MAIL}</a></li>
          <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg><span>Av. Luiz Dumont Villares, 2078 — CJ 78<br>Parada Inglesa, São Paulo — SP<br>02239-000</span></li>
        </ul>
      </div>
    </div>
    <div class="footer__bar">
      <span>© 1998–<span data-year>2026</span> Wicorp — Conexões Inteligentes. Todos os direitos reservados.</span>
      <span><a href="{prefix}privacidade.html">Política de Privacidade</a> · LGPD</span>
    </div>
  </div>
</footer>
{wa(prefix)}
<script src="{prefix}js/main.js"></script>
</body>
</html>
"""


def wa(prefix):
    return (f'<a href="https://wa.me/{WPP_HREF}" class="wa-float" data-pos="flutuante" target="_blank" '
            f'rel="noopener" aria-label="Falar com a Wicorp no WhatsApp">'
            f'<svg width="27" height="27" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
            f'<path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.39-1.47-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.01-1.04 2.47 0 1.46 1.06 2.87 1.21 3.07.15.2 2.09 3.2 5.07 4.49.71.3 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.28.17-1.41-.07-.13-.27-.2-.57-.35M12.04 21.5h-.01c-1.75 0-3.47-.47-4.97-1.36l-.36-.21-3.7.97.99-3.6-.23-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.89 9.9-9.89 2.64 0 5.12 1.03 6.99 2.9a9.82 9.82 0 0 1 2.89 6.99c0 5.45-4.44 9.89-9.89 9.89m8.42-18.31A11.8 11.8 0 0 0 12.04 0C5.46 0 .1 5.35.1 11.93c0 2.1.55 4.16 1.6 5.97L0 24l6.25-1.64a11.9 11.9 0 0 0 5.79 1.47h.01c6.58 0 11.93-5.35 11.94-11.93a11.86 11.86 0 0 0-3.48-8.44"/></svg></a>')


def crumb(prefix, label):
    sep = ('<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<polyline points="9 18 15 12 9 6"/></svg>')
    return (f'<nav class="crumb" aria-label="Você está em"><a href="{prefix}index.html">Início</a>{sep}'
            f'<a href="{prefix}index.html#solucoes">Soluções</a>{sep}<span>{label}</span></nav>')


def form(form_id, solucao, titulo, sub, botao, prefix=""):
    p = form_id
    return f"""
<aside class="form-card" id="form">
  <div class="form-card__head">
    <h3>{titulo}</h3>
    <p>{sub}</p>
  </div>
  <form data-wicorp-form data-form-id="{form_id}" data-solucao="{solucao}" novalidate>
    <div class="field">
      <label for="{p}-nome">Nome</label>
      <input type="text" id="{p}-nome" name="nome" placeholder="Como podemos te chamar" required autocomplete="name">
      <span class="field__err"></span>
    </div>
    <div class="field">
      <label for="{p}-email">E-mail corporativo</label>
      <input type="email" id="{p}-email" name="email" placeholder="voce@suaempresa.com.br" required autocomplete="email">
      <span class="field__err"></span>
    </div>
    <div class="field">
      <label for="{p}-empresa">Empresa</label>
      <input type="text" id="{p}-empresa" name="empresa" placeholder="Razão social ou nome fantasia" required autocomplete="organization">
      <span class="field__err"></span>
    </div>
    <div class="field">
      <label for="{p}-whats">WhatsApp</label>
      <input type="tel" id="{p}-whats" name="whatsapp" placeholder="(11) 90000-0000" required autocomplete="tel" inputmode="numeric">
      <span class="field__err"></span>
    </div>
    <button type="submit" class="btn btn--primary btn--wide" data-label="{botao}">{botao}</button>
    <p class="form-note">Retornamos em até 1 dia útil. Seus dados não são compartilhados com terceiros.</p>
  </form>
  <div class="form-alt">
    Prefere conversar agora?
    <a href="https://wa.me/{WPP_HREF}" data-pos="form-{form_id}" target="_blank" rel="noopener">Chamar no WhatsApp</a>
  </div>
  <div class="form-success">
    <svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
    <h3>Recebemos sua solicitação</h3>
    <p>Um especialista da Wicorp entra em contato em até 1 dia útil.</p>
  </div>
</aside>
"""


def proof_band():
    return """
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
"""


def cta_band(titulo, texto, botao, href="#form", tel=True):
    extra = (f'<a href="tel:{TEL_HREF}" class="btn btn--ghost btn--wide">Ligar: {TEL}</a>') if tel else ""
    return f"""
<section class="section section--tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <div class="cta-band__inner">
        <div>
          <h2 class="display">{titulo}</h2>
          <p class="lead">{texto}</p>
        </div>
        <div class="cta-band__actions">
          <a href="{href}" class="btn btn--primary btn--wide">{botao}
            <svg class="arrow" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          {extra}
        </div>
      </div>
    </div>
  </div>
</section>
"""


CHECK = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<polyline points="20 6 9 17 4 12"/></svg>')


def checklist(items):
    li = "".join(f"<li>{CHECK}<span>{i}</span></li>" for i in items)
    return f'<ul class="checklist">{li}</ul>'


def faq(pairs):
    body = "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in pairs)
    return f'<div class="faq">{body}</div>'


def faq_schema(pairs):
    import json
    data = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


# ===========================================================================
# PÁGINAS DE SOLUÇÃO
# ===========================================================================
P = "../"   # prefixo para páginas em subpasta


# --------------------------------------------------------------------------
# 1. LINK DEDICADO E LINK.BOX
# --------------------------------------------------------------------------
FAQ_LINK = [
    ("Qual a diferença entre link dedicado e banda larga comum?",
     "Banda larga é compartilhada com outros assinantes e a velocidade contratada é um teto, não uma garantia. "
     "O link dedicado entrega banda garantida, simétrica, com IP fixo e SLA contratual — a mesma velocidade de "
     "subida e descida, a qualquer hora do dia."),
    ("Como funciona o backup automático do Link.Box?",
     "O Link.Box monitora a conexão principal continuamente. Quando detecta queda ou degradação, comuta o tráfego "
     "para dois chips 4G/5G de operadoras diferentes, sem intervenção manual. Quando o link principal volta, "
     "a comutação é revertida automaticamente."),
    ("Preciso trocar meu link atual para usar o Link.Box?",
     "Não. O Link.Box trabalha sobre a conexão que você já tem, inclusive de outra operadora. Muitos clientes "
     "começam mantendo o link atual e adicionando apenas a camada de redundância."),
    ("Em quanto tempo o link é ativado?",
     "Depende da viabilidade técnica no endereço. Em regiões com fibra já instalada, a ativação costuma ocorrer "
     "em poucos dias. A consulta de disponibilidade responde isso antes de qualquer proposta."),
    ("Vocês atendem operações com várias filiais?",
     "Sim — é um dos cenários mais comuns. Redes de varejo, farmácias e operações distribuídas usam o Link.Box "
     "justamente para que um PDV isolado não pare por falha de uma única operadora."),
]

BODY_LINK = f"""
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        {crumb(P, "Link dedicado e Link.Box")}
        <span class="eyebrow">Conectividade empresarial</span>
        <h1 class="display">Link dedicado empresarial com <span class="grad-text">backup automático 4G/5G</span></h1>
        <p class="lead">Sua operação continua online mesmo quando a conexão principal cai. Banda garantida,
        IP fixo, monitoramento 24/7 e redundância que age sozinha.</p>
        <div class="hero__actions">
          <a href="#form" class="btn btn--primary">Consultar disponibilidade no meu endereço
            <svg class="arrow" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="https://wa.me/{WPP_HREF}" data-pos="hero-link" class="btn btn--ghost" target="_blank" rel="noopener">Falar com um especialista</a>
        </div>
        <div class="hero__seals">
          <div class="seal">{CHECK} Banda garantida e simétrica</div>
          <div class="seal">{CHECK} IP fixo incluso</div>
          <div class="seal">{CHECK} SLA contratual</div>
        </div>
      </div>
      {form("link", "link-dedicado", "Consulte a disponibilidade",
            "Informe seus dados e verificamos a viabilidade técnica no endereço da sua operação.",
            "Consultar disponibilidade")}
    </div>
  </div>
</section>

{proof_band()}

{sections.FAILOVER_ALT}

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Por que isso importa</span>
      <h2 class="display">Se a internet principal cair agora, sua operação para?</h2>
      <p class="lead">A maioria das empresas descobre que não tinha plano B no dia em que precisou dele.</p>
    </div>
    <div class="grid grid--3">
      <div class="pain reveal">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="1" y="4" width="22" height="16" rx="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg></div>
        <div><h3>PDV sem conexão não fatura</h3><p>Cada minuto de loja parada é venda que não acontece — e cliente que vai embora sem esperar.</p></div>
      </div>
      <div class="pain reveal" data-d="1">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
        <div><h3>Filial isolada trava o time inteiro</h3><p>Sem conexão, a unidade perde acesso a sistemas, telefonia e ao restante da empresa ao mesmo tempo.</p></div>
      </div>
      <div class="pain reveal" data-d="2">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg></div>
        <div><h3>Sistema em nuvem fora do ar</h3><p>ERP, emissor fiscal e atendimento dependem da conexão. Sem ela, a operação inteira fica cega.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Como funciona na prática</span>
      <h2 class="display">Três níveis de proteção da conexão</h2>
      <p class="lead">Este é o comparativo que costuma decidir a conversa. A diferença não está na velocidade —
      está no que acontece quando algo falha.</p>
    </div>
    <div class="table-scroll reveal">
      <table class="compare">
        <thead><tr><th>Cenário</th><th>Link único</th><th>Dois links, mesma operadora</th><th>Link.Box com backup 4G/5G</th></tr></thead>
        <tbody>
          <tr><td>Queda da operadora principal</td><td class="no">Operação para</td><td class="no">Ambos caem juntos</td><td class="yes">Comuta automaticamente</td></tr>
          <tr><td>Tempo de indisponibilidade</td><td>Horas, até o reparo</td><td>Horas, se a falha for na operadora</td><td class="yes">Segundos</td></tr>
          <tr><td>Ação necessária da equipe</td><td>Abrir chamado e aguardar</td><td>Trocar manualmente</td><td class="yes">Nenhuma</td></tr>
          <tr><td>Visibilidade da falha</td><td class="no">Só quando o usuário reclama</td><td>Parcial</td><td class="yes">Alerta do NOC em tempo real</td></tr>
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
        <span class="eyebrow">O que está incluído</span>
        <h2 class="display" style="margin-bottom:20px">Conectividade preparada para operação crítica</h2>
        <p class="lead" style="margin-bottom:24px">Conectividade empresarial vai além de contratar internet.
        Ela precisa acompanhar as necessidades e os riscos da operação.</p>
        {checklist([
          "Link dedicado via fibra óptica ou rádio",
          "Banda garantida e simétrica, com IP fixo",
          "Redundância automática por dois chips 4G/5G",
          "Monitoramento proativo 24/7 pelo nosso NOC",
          "SLA contratual com prazo de atendimento definido",
          "Suporte técnico próprio, sem fila de operadora",
        ])}
      </div>
      <div class="callout">
        <h3>Link.Box: tecnologia proprietária da Wicorp</h3>
        <p>O Link.Box é o equipamento que gerencia diferentes conexões e cria uma estrutura de redundância real
        para a empresa. Ele não depende de uma única operadora — combina o link cabeado com dois chips de
        operadoras distintas.</p>
        <p>Hoje são mais de 700 equipamentos em operação em redes de varejo, farmácias, indústrias e
        instituições de ensino em todo o Brasil.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="split--wide-left split reveal">
      <div>
        <span class="eyebrow">Como começamos</span>
        <h2 class="display" style="margin-bottom:32px">Do primeiro contato à ativação</h2>
        <ol class="steps">
          <li><h3>Consulta de disponibilidade</h3><p>Verificamos a viabilidade técnica no endereço da sua operação — antes de qualquer proposta.</p></li>
          <li><h3>Diagnóstico da estrutura atual</h3><p>Nossa equipe mapeia onde existe ponto único de falha e o que já pode ser aproveitado.</p></li>
          <li><h3>Desenho da arquitetura</h3><p>Definimos banda, redundância e SLA a partir da sua operação, não de um pacote pronto.</p></li>
          <li><h3>Instalação e ativação</h3><p>Equipe própria em campo, com testes de comutação validados antes da entrega.</p></li>
          <li><h3>Monitoramento contínuo</h3><p>O NOC passa a acompanhar o link 24/7 e age antes que a falha chegue ao seu usuário.</p></li>
        </ol>
      </div>
      <div>
        <div class="card">
          <h3 style="font-size:1.1rem;margin-bottom:12px">Já é cliente Wicorp?</h3>
          <p style="font-size:.92rem;color:var(--tx-2);line-height:1.7;margin-bottom:20px">
            Se você já tem link dedicado conosco e ainda não tem a camada de redundância,
            vale conversar. Na maioria dos casos o Link.Box é adicionado sem trocar nada
            da estrutura existente.</p>
          <a href="https://wa.me/{WPP_HREF}" data-pos="ja-cliente" class="btn btn--ghost btn--wide" target="_blank" rel="noopener">Falar com meu consultor</a>
        </div>
      </div>
    </div>
  </div>
</section>

{sections.mockup_section("Sua rede acompanhada em tempo real", "Monitoramento 24/7", "Nosso NOC acompanha cada link continuamente. Quando algo sai do padrão, o alerta chega para a nossa equipe antes de chegar ao seu usuário.", sections.MOCK_NOC, [("24/7", "acompanhamento do NOC"), ("+700", "equipamentos monitorados"), ("SLA", "prazo em contrato")])}

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Perguntas frequentes</span>
      <h2 class="display">Dúvidas de quem está avaliando</h2>
    </div>
    <div class="reveal">{faq(FAQ_LINK)}</div>
  </div>
</section>

{cta_band("Descubra onde sua rede está vulnerável",
          "Avaliamos sua estrutura atual e mostramos onde existe ponto único de falha. Sem compromisso.",
          "Solicitar avaliação da minha rede")}
</main>
"""


# --------------------------------------------------------------------------
# 2. PABX VIRTUAL EM NUVEM
# --------------------------------------------------------------------------
FAQ_PABX = [
    ("Preciso trocar meus números de telefone?",
     "Não. Fazemos a portabilidade dos números atuais, inclusive os fixos que sua empresa já divulga. "
     "O cliente continua ligando para o mesmo número."),
    ("O que acontece se a internet cair?",
     "As chamadas podem ser desviadas automaticamente para celulares definidos por você. Em operações críticas, "
     "combinamos o PABX virtual com o Link.Box, e a redundância 4G/5G mantém a telefonia funcionando."),
    ("A equipe consegue atender de casa ou em viagem?",
     "Sim. O ramal funciona pelo aplicativo no celular ou pelo computador, com o mesmo número e as mesmas "
     "permissões de quando a pessoa está no escritório."),
    ("Como funciona a integração com WhatsApp?",
     "As conversas de WhatsApp entram na mesma plataforma das ligações, distribuídas por fila e por responsável. "
     "O histórico fica registrado na empresa, não no celular pessoal do vendedor."),
    ("O que a IA faz no atendimento?",
     "Recursos como URA inteligente, transcrição de chamadas e distribuição automática por assunto. "
     "O objetivo é reduzir transferência desnecessária e dar visibilidade do que foi tratado."),
]

BODY_PABX = f"""
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        {crumb(P, "PABX virtual com IA")}
        <span class="eyebrow">Comunicação corporativa</span>
        <h1 class="display">PABX virtual em nuvem para empresas, com <span class="grad-text">IA e atendimento integrado</span></h1>
        <p class="lead">Ligações, ramais, WhatsApp e atendimento reunidos em uma única plataforma —
        com relatórios em tempo real e visibilidade de tudo que acontece.</p>
        <div class="hero__actions">
          <a href="#form" class="btn btn--primary">Simular meu plano
            <svg class="arrow" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="https://wa.me/{WPP_HREF}" data-pos="hero-pabx" class="btn btn--ghost" target="_blank" rel="noopener">Falar com um especialista</a>
        </div>
        <div class="hero__seals">
          <div class="seal">{CHECK} Portabilidade dos seus números</div>
          <div class="seal">{CHECK} Ramal no celular e no desktop</div>
          <div class="seal">{CHECK} Relatórios em tempo real</div>
        </div>
      </div>
      {form("pabx", "pabx-virtual", "Simule seu plano",
            "Informe seus dados e montamos uma simulação a partir do número de ramais da sua operação.",
            "Simular meu plano")}
    </div>
  </div>
</section>

{proof_band()}

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Situações que você reconhece</span>
      <h2 class="display">Seu atendimento evoluiu. Sua telefonia acompanhou?</h2>
    </div>
    <div class="grid grid--3">
      <div class="pain reveal">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/><line x1="23" y1="1" x2="17" y2="7"/></svg></div>
        <div><h3>Cliente que cai na linha ocupada</h3><p>Sem fila e sem distribuição, quem liga em horário de pico simplesmente não é atendido — e liga para o concorrente.</p></div>
      </div>
      <div class="pain reveal" data-d="1">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8z"/></svg></div>
        <div><h3>Conversa que some com o vendedor</h3><p>Atendimento que começa no WhatsApp pessoal desaparece quando a pessoa sai de férias — ou da empresa.</p></div>
      </div>
      <div class="pain reveal" data-d="2">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></div>
        <div><h3>Nenhum número para acompanhar</h3><p>Quantas ligações foram perdidas ontem? Quanto tempo o cliente esperou? Sem relatório, a gestão vira achismo.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">PABX físico × PABX em nuvem</span>
      <h2 class="display">Cinco diferenças que impactam o bolso</h2>
      <p class="lead">A inércia tecnológica costuma custar mais caro que a mudança.</p>
    </div>
    <div class="table-scroll reveal">
      <table class="compare">
        <thead><tr><th></th><th>PABX físico tradicional</th><th>PABX virtual Wicorp</th></tr></thead>
        <tbody>
          <tr><td>Investimento inicial</td><td class="no">Compra do equipamento e instalação</td><td class="yes">Sem hardware, custo mensal por ramal</td></tr>
          <tr><td>Manutenção</td><td class="no">Técnico presencial a cada ajuste</td><td class="yes">Configuração remota e imediata</td></tr>
          <tr><td>Trabalho remoto</td><td class="no">Preso ao aparelho no escritório</td><td class="yes">Ramal no celular e no computador</td></tr>
          <tr><td>Crescer ou reduzir ramais</td><td class="no">Novo projeto e nova licença</td><td class="yes">Ajuste no painel, no mesmo dia</td></tr>
          <tr><td>Relatórios de atendimento</td><td class="no">Inexistentes ou manuais</td><td class="yes">Em tempo real, por fila e por atendente</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">A plataforma</span>
      <h2 class="display">Três módulos, uma única solução</h2>
    </div>
    <div class="grid grid--3">
      <article class="sol reveal">
        <div class="sol__ico"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg></div>
        <span class="sol__tag">Telefonia</span>
        <h3>Phone System</h3>
        <p>Ramais em nuvem, URA inteligente, filas de atendimento e portabilidade dos números que sua empresa já usa.</p>
        <ul class="sol__list"><li>Ramal no celular e desktop</li><li>URA com roteamento por assunto</li><li>Gravação de chamadas</li></ul>
      </article>
      <article class="sol reveal" data-d="1">
        <div class="sol__ico"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
        <span class="sol__tag">Omnichannel</span>
        <h3>Customer Experience</h3>
        <p>WhatsApp, chat e e-mail no mesmo painel das ligações, com histórico que fica na empresa.</p>
        <ul class="sol__list"><li>WhatsApp corporativo com filas</li><li>Histórico centralizado</li><li>Distribuição por responsável</li></ul>
      </article>
      <article class="sol reveal" data-d="2">
        <div class="sol__ico"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/></svg></div>
        <span class="sol__tag">Atendimento</span>
        <h3>Contact Center</h3>
        <p>Operação de atendimento estruturada, com supervisão em tempo real e indicadores por atendente.</p>
        <ul class="sol__list"><li>Painel de supervisão ao vivo</li><li>Indicadores por fila</li><li>Recursos de IA aplicados</li></ul>
      </article>
    </div>
  </div>
</section>

{sections.mockup_section("O painel que sua equipe usa todo dia", "A plataforma por dentro", "Ligações, WhatsApp e chat na mesma tela, com tempo de espera e status de cada atendente à vista.", sections.MOCK_PABX, [("1 painel", "todos os canais"), ("Tempo real", "supervisão da fila"), ("IA", "roteamento por assunto")])}

{sections.DIMENSIONADOR}

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Perguntas frequentes</span>
      <h2 class="display">Dúvidas de quem está avaliando</h2>
    </div>
    <div class="reveal">{faq(FAQ_PABX)}</div>
  </div>
</section>

{cta_band("Veja quanto sua telefonia pode ficar mais simples",
          "Montamos uma simulação a partir do número de ramais e do perfil de atendimento da sua empresa.",
          "Simular meu plano agora")}
</main>
"""


# --------------------------------------------------------------------------
# 3. FIREWALL E SD-WAN
# --------------------------------------------------------------------------
FAQ_FW = [
    ("Meu roteador já tem firewall. Isso não basta?",
     "O firewall de um roteador comum filtra portas e endereços. Um firewall de próxima geração enxerga a "
     "aplicação em si — identifica que o tráfego é streaming, jogo, armazenamento em nuvem ou ferramenta não "
     "autorizada, mesmo quando tudo passa pela mesma porta."),
    ("O que significam MDR e SOC?",
     "SOC é o centro de operações de segurança: uma equipe monitorando eventos da sua rede. MDR é a detecção e "
     "resposta gerenciada — quando essa equipe não apenas identifica o incidente, mas age para contê-lo. "
     "Na prática, alguém está olhando mesmo quando ninguém da sua empresa está."),
    ("Isso ajuda na adequação à LGPD?",
     "Ajuda em uma parte importante dela. A LGPD exige medidas técnicas de proteção dos dados pessoais que a "
     "empresa trata, e exige comunicar incidentes. Firewall, segmentação de rede e registro de eventos sustentam "
     "essas duas obrigações — mas adequação completa envolve também processo e jurídico."),
    ("Vocês assumem a gestão ou só instalam?",
     "Assumimos a gestão. O equipamento é configurado, monitorado e ajustado pela nossa equipe, com relatórios "
     "periódicos. Você não fica com um appliance caro sem ninguém para operá-lo."),
    ("E se a empresa tiver várias unidades?",
     "É justamente onde o SD-WAN entra: ele conecta as unidades com política de segurança única e distribui o "
     "tráfego entre os links disponíveis, priorizando o que é crítico para a operação."),
]

BODY_FW = f"""
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        {crumb(P, "Firewall e SD-WAN")}
        <span class="eyebrow">Cibersegurança corporativa</span>
        <h1 class="display">Firewall corporativo, SD-WAN e <span class="grad-text">proteção de rede gerenciada</span></h1>
        <p class="lead">Visibilidade de quem acessa o quê, quanta banda cada aplicação consome e onde estão
        os riscos — com monitoramento 24/7 e resposta a incidentes.</p>
        <div class="hero__actions">
          <a href="#form" class="btn btn--primary">Solicitar diagnóstico de cibersegurança
            <svg class="arrow" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="https://wa.me/{WPP_HREF}" data-pos="hero-fw" class="btn btn--ghost" target="_blank" rel="noopener">Falar com um especialista</a>
        </div>
        <div class="hero__seals">
          <div class="seal">{CHECK} Gestão inclusa, não só o equipamento</div>
          <div class="seal">{CHECK} Monitoramento 24/7</div>
          <div class="seal">{CHECK} Alinhado às exigências da LGPD</div>
        </div>
      </div>
      {form("fw", "firewall-sdwan", "Diagnóstico de cibersegurança",
            "Avaliamos a exposição da sua rede e entregamos um relatório com os pontos que precisam de atenção.",
            "Solicitar diagnóstico")}
    </div>
  </div>
</section>

{proof_band()}

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">O risco real, sem alarmismo</span>
      <h2 class="display">Você sabe quem está acessando o quê na sua rede agora?</h2>
      <p class="lead">Não se trata de ataque hollywoodiano. Trata-se de consequências mensuráveis
      que aparecem no dia a dia de operações comuns.</p>
    </div>
    <div class="grid grid--3">
      <div class="pain reveal">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></div>
        <div><h3>Dado de cliente exposto tem implicação legal</h3><p>Sob a LGPD, vazamento não é só problema técnico: envolve notificação, apuração e possível sanção.</p></div>
      </div>
      <div class="pain reveal" data-d="1">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div>
        <div><h3>Rede sem segmentação propaga o incidente</h3><p>Um único computador comprometido alcança servidores, backups e as demais unidades sem nenhuma barreira no caminho.</p></div>
      </div>
      <div class="pain reveal" data-d="2">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13.73 21a2 2 0 0 1-3.46 0"/><path d="M18.63 13A17.89 17.89 0 0 1 18 8"/><path d="M6.26 6.26A5.86 5.86 0 0 0 6 8c0 7-3 9-3 9h14"/><path d="M18 8a6 6 0 0 0-9.33-5"/><line x1="1" y1="1" x2="23" y2="23"/></svg></div>
        <div><h3>Sem registro, ninguém sabe o que aconteceu</h3><p>Quando não há log nem monitoramento, a empresa descobre a falha depois do impacto — e não consegue explicar a origem.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <span class="eyebrow">Traduzindo o técnico</span>
        <h2 class="display" style="margin-bottom:20px">O que um firewall de próxima geração enxerga</h2>
        <p class="lead" style="margin-bottom:24px">Um roteador comum vê endereços e portas. Um firewall de
        próxima geração vê a aplicação, o usuário e o comportamento — e é isso que permite decidir o que
        bloquear sem travar o trabalho de ninguém.</p>
        {checklist([
          "Qual aplicação está consumindo a banda, não só qual porta",
          "Qual usuário fez o acesso, e de qual dispositivo",
          "Tentativas de conexão com destinos maliciosos conhecidos",
          "Tráfego criptografado que esconde ferramenta não autorizada",
          "Padrões fora do normal para aquele horário e aquele setor",
          "Registro completo para auditoria e resposta a incidente",
        ])}
      </div>
      <div class="callout">
        <h3>Segurança gerenciada, não appliance esquecido</h3>
        <p>O erro mais comum que encontramos é a empresa ter comprado um bom equipamento e nunca ter tido
        quem o configurasse direito. Regra padrão de fábrica, firmware de três anos atrás e nenhum alerta
        chegando a ninguém.</p>
        <p>Aqui o equipamento vem com gestão: configuração, atualização, monitoramento pelo nosso NOC e
        relatório periódico do que aconteceu na sua rede.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">O que está incluído</span>
      <h2 class="display">Três camadas de proteção</h2>
    </div>
    <div class="grid grid--3">
      <article class="sol reveal">
        <div class="sol__ico"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <span class="sol__tag">Perímetro</span>
        <h3>Firewall de próxima geração</h3>
        <p>Controle de aplicação, filtro de conteúdo, VPN para acesso remoto e inspeção de tráfego criptografado.</p>
      </article>
      <article class="sol reveal" data-d="1">
        <div class="sol__ico"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><circle cx="5" cy="5" r="2"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><line x1="6.5" y1="6.5" x2="10" y2="10"/><line x1="17.5" y1="6.5" x2="14" y2="10"/><line x1="6.5" y1="17.5" x2="10" y2="14"/><line x1="17.5" y1="17.5" x2="14" y2="14"/></svg></div>
        <span class="sol__tag">Multiunidade</span>
        <h3>SD-WAN</h3>
        <p>Unidades conectadas com política única, priorização do tráfego crítico e uso inteligente dos links disponíveis.</p>
      </article>
      <article class="sol reveal" data-d="2">
        <div class="sol__ico"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div>
        <span class="sol__tag">Estação</span>
        <h3>Antivírus corporativo</h3>
        <p>Proteção de endpoint com console central, com opção de MDR e SOC 24/7 para detecção e resposta gerenciada.</p>
      </article>
    </div>
  </div>
</section>

{sections.mockup_section("O que passa a ficar visível", "Visibilidade da rede", "Sem firewall gerenciado, ninguém sabe qual aplicação consome a banda nem o que foi bloqueado. Com ele, isso vira relatório.", sections.MOCK_FW, [("1.284", "ameaças bloqueadas no mês"), ("142", "dispositivos mapeados"), ("LGPD", "registro para auditoria")])}

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Perguntas frequentes</span>
      <h2 class="display">Dúvidas de quem está avaliando</h2>
    </div>
    <div class="reveal">{faq(FAQ_FW)}</div>
  </div>
</section>

{cta_band("Solicite um diagnóstico da sua rede",
          "Avaliamos a exposição da sua estrutura e entregamos um relatório com os pontos que precisam de atenção. Sem compromisso.",
          "Solicitar diagnóstico de cibersegurança")}
</main>
"""


# --------------------------------------------------------------------------
# 4. INFRAESTRUTURA E PROJETOS
# --------------------------------------------------------------------------
FAQ_INFRA = [
    ("Vocês fazem o projeto ou só executam?",
     "Fazemos as duas coisas. O levantamento em campo, o projeto executivo, a execução e a documentação final "
     "ficam com a mesma equipe — o que evita o repasse de responsabilidade entre projetista e instalador."),
    ("Atendem obras em operação, sem parar a empresa?",
     "Sim. Boa parte dos projetos é executada em ambiente ativo, com etapas planejadas em horários combinados "
     "para não interromper o funcionamento."),
    ("O que entra na documentação da entrega?",
     "Projeto as-built, identificação de pontos, certificação dos cabos, diagrama lógico e inventário dos "
     "equipamentos instalados. É o que permite que qualquer técnico entenda a rede depois."),
    ("Vocês atendem fora de São Paulo?",
     "Nossa operação com SLA garantido é concentrada em São Paulo e Grande São Paulo. Projetos fora dessa "
     "região são avaliados caso a caso, para não prometer um nível de atendimento que não conseguimos manter."),
]

BODY_INFRA = f"""
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        {crumb(P, "Infraestrutura e projetos")}
        <span class="eyebrow">Projetos e suporte</span>
        <h1 class="display">Projetos de infraestrutura de TI, <span class="grad-text">cabeamento estruturado e suporte técnico</span></h1>
        <p class="lead">Da consultoria à execução, com uma equipe que continua acompanhando sua operação
        depois que a obra termina.</p>
        <div class="hero__actions">
          <a href="#form" class="btn btn--primary">Solicitar uma avaliação da estrutura
            <svg class="arrow" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="https://wa.me/{WPP_HREF}" data-pos="hero-infra" class="btn btn--ghost" target="_blank" rel="noopener">Falar com um especialista</a>
        </div>
        <div class="hero__seals">
          <div class="seal">{CHECK} Equipe própria em campo</div>
          <div class="seal">{CHECK} Projeto as-built documentado</div>
          <div class="seal">{CHECK} Suporte após a entrega</div>
        </div>
      </div>
      {form("infra", "infraestrutura", "Avalie sua estrutura atual",
            "Nossa equipe faz o levantamento e aponta o que precisa ser adequado antes de qualquer proposta.",
            "Solicitar avaliação")}
    </div>
  </div>
</section>

{proof_band()}

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">O que costumamos encontrar</span>
      <h2 class="display">Infraestrutura improvisada cobra o preço depois</h2>
      <p class="lead">Rede montada às pressas funciona no primeiro mês. O problema aparece quando a empresa cresce.</p>
    </div>
    <div class="grid grid--2">
      <div class="pain reveal">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="6" y1="3" x2="6" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/></svg></div>
        <div><h3>Ninguém sabe qual cabo vai para onde</h3><p>Sem identificação nem documentação, cada manutenção vira investigação — e o técnico cobra pelas horas de descoberta.</p></div>
      </div>
      <div class="pain reveal" data-d="1">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/></svg></div>
        <div><h3>Wi-Fi que cai nas áreas que mais importam</h3><p>Roteador doméstico em ambiente corporativo não sustenta densidade de usuários nem cobre o galpão inteiro.</p></div>
      </div>
      <div class="pain reveal" data-d="2">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg></div>
        <div><h3>Câmera instalada que não grava nada</h3><p>CFTV sem dimensionamento de armazenamento grava por poucos dias — e a imagem que interessa já foi sobrescrita.</p></div>
      </div>
      <div class="pain reveal" data-d="3">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg></div>
        <div><h3>A obra acaba e o fornecedor some</h3><p>Entrega feita, contrato encerrado. Quando o problema aparece seis meses depois, não há a quem recorrer.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">O que executamos</span>
      <h2 class="display">Projetos completos de TI, redes e telecom</h2>
    </div>
    <div class="grid grid--4">
      <article class="sol reveal">
        <div class="sol__ico"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg></div>
        <h3>Cabeamento estruturado</h3>
        <p>Projeto, execução, certificação e documentação as-built de toda a malha de rede.</p>
      </article>
      <article class="sol reveal" data-d="1">
        <div class="sol__ico"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/></svg></div>
        <h3>Wi-Fi corporativo</h3>
        <p>Site survey, dimensionamento por densidade e controladora com gestão centralizada.</p>
      </article>
      <article class="sol reveal" data-d="2">
        <div class="sol__ico"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg></div>
        <h3>Segurança e CFTV</h3>
        <p>Câmeras, gravação dimensionada e acesso remoto às imagens com controle de permissão.</p>
      </article>
      <article class="sol reveal" data-d="3">
        <div class="sol__ico"><svg width="25" height="25" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/></svg></div>
        <h3>Monitoramento e suporte</h3>
        <p>Acompanhamento contínuo do ambiente e suporte técnico com SLA definido em contrato.</p>
      </article>
    </div>
  </div>
</section>

{sections.mockup_section("Sua rede documentada, não improvisada", "O que entra na entrega", "Cada ponto identificado, cada cabo certificado e um diagrama que qualquer técnico entende depois — inclusive daqui a três anos.", sections.MOCK_INFRA, [("as-built", "projeto entregue"), ("100%", "pontos certificados"), ("SLA 4h", "atendimento em campo")], alt=True)}

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Perguntas frequentes</span>
      <h2 class="display">Dúvidas de quem está avaliando</h2>
    </div>
    <div class="reveal">{faq(FAQ_INFRA)}</div>
  </div>
</section>

{cta_band("Vamos avaliar sua estrutura atual",
          "Nossa equipe faz o levantamento em campo e aponta o que precisa ser adequado — antes de qualquer proposta.",
          "Solicitar uma avaliação")}
</main>
"""


# ===========================================================================
# LANDING PAGE 4 — CENTRALIZAÇÃO DE FORNECEDORES
# Vende o posicionamento central, não produto. É a mais estratégica.
# ===========================================================================
BODY_LP = f"""
<main id="main">
<section class="page-hero" style="padding-top:calc(var(--header-h) + 54px)">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        <span class="eyebrow">Para gestores de TI · São Paulo e Grande SP</span>
        <h1 class="display">Quantos fornecedores sua equipe precisa acionar <span class="grad-text">quando algo para?</span></h1>
        <p class="lead">Internet, telefonia, firewall, suporte e infraestrutura com um único contrato,
        um único contato e uma equipe que conhece sua operação inteira.</p>
        <div class="hero__seals" style="border-top:none; padding-top:0">
          <div class="seal">{CHECK} 28 anos de mercado</div>
          <div class="seal">{CHECK} +800 clientes ativos</div>
          <div class="seal">{CHECK} NOC próprio 24/7</div>
        </div>
      </div>
      {form("lp-central", "centralizacao", "Mapeamos seus fornecedores atuais",
            "Sem compromisso: mostramos o que dá para centralizar, o que faz sentido manter e onde está o retrabalho da sua equipe.",
            "Quero o mapeamento gratuito")}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">A rotina que ninguém escolheu</span>
      <h2 class="display">O gestor de TI virou integrador sem querer</h2>
      <p class="lead">Quando a operação para, começa a maratona. E ela raramente é técnica —
      é de coordenação entre fornecedores que não se falam.</p>
    </div>
    <div class="grid grid--2">
      <div class="pain reveal">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/></svg></div>
        <div><h3>Chamado aberto em três portais diferentes</h3><p>Cada fornecedor com seu sistema, seu protocolo e seu prazo. Ninguém cruza as informações.</p></div>
      </div>
      <div class="pain reveal" data-d="1">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg></div>
        <div><h3>Cada um aponta para o outro</h3><p>A operadora diz que é o firewall. O firewall diz que é o link. E a operação segue parada enquanto isso se resolve.</p></div>
      </div>
      <div class="pain reveal" data-d="2">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/><line x1="2" y1="2" x2="22" y2="22"/></svg></div>
        <div><h3>Ninguém enxerga o ambiente completo</h3><p>Cada fornecedor vê seu pedaço. A visão do todo existe só na cabeça de quem gerencia — e sai de férias junto com ele.</p></div>
      </div>
      <div class="pain reveal" data-d="3">
        <div class="pain__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
        <div><h3>Custos espalhados, sem previsibilidade</h3><p>Cinco faturas, cinco reajustes em datas diferentes. Ninguém consegue dizer quanto custa manter a operação conectada.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">O que muda</span>
      <h2 class="display">Menos fornecedores. Menos incêndios.</h2>
    </div>
    <div class="vs reveal">
      <div class="vs__col vs__col--before">
        <div class="vs__lbl">Hoje</div>
        <h3>Cinco fornecedores, cinco contratos</h3>
        <ul>
          <li><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg> Operadora de internet</li>
          <li><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg> Empresa de telefonia</li>
          <li><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg> Fornecedor de firewall</li>
          <li><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg> Helpdesk terceirizado</li>
          <li><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg> Prestador de infraestrutura</li>
        </ul>
      </div>
      <div class="vs__mid"><div class="vs__arrow"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div></div>
      <div class="vs__col vs__col--after">
        <div class="vs__lbl">Com a Wicorp</div>
        <h3>Um parceiro entre você e a complexidade</h3>
        <ul>
          <li><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg> Um contrato, um contato</li>
          <li><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg> Equipe que conhece todo o ambiente</li>
          <li><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg> Monitoramento antes da reclamação</li>
          <li><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg> Custo centralizado e previsível</li>
          <li><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg> Sua equipe de volta à estratégia</li>
        </ul>
      </div>
    </div>
  </div>
</section>

{proof_band()}

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">O ecossistema completo</span>
      <h2 class="display">Tudo que hoje está espalhado, em um lugar só</h2>
    </div>
    <div class="grid grid--4">
      <div class="card reveal"><h3 style="font-size:1rem;margin-bottom:8px">Conectividade</h3><p style="font-size:.87rem;color:var(--tx-3);line-height:1.6">Link dedicado, Link.Box com backup 4G/5G, SD-WAN</p></div>
      <div class="card reveal" data-d="1"><h3 style="font-size:1rem;margin-bottom:8px">Comunicação</h3><p style="font-size:.87rem;color:var(--tx-3);line-height:1.6">PABX virtual com IA, SIP Trunk, Contact Center</p></div>
      <div class="card reveal" data-d="2"><h3 style="font-size:1rem;margin-bottom:8px">Segurança</h3><p style="font-size:.87rem;color:var(--tx-3);line-height:1.6">Firewall gerenciado, antivírus corporativo, CFTV</p></div>
      <div class="card reveal" data-d="3"><h3 style="font-size:1rem;margin-bottom:8px">Infraestrutura</h3><p style="font-size:.87rem;color:var(--tx-3);line-height:1.6">Cabeamento, Wi-Fi corporativo, suporte com SLA</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Quem já centralizou</span>
      <h2 class="display">O que mudou para eles</h2>
    </div>
    <div class="grid grid--2">
      <figure class="quote reveal">
        <div class="quote__mark">"</div>
        <p>Iniciamos a parceria em 2018 e trouxe economia absurda. O valor caiu drasticamente, com melhorias em processos.</p>
        <figcaption class="quote__who"><div class="quote__av">VT</div><div><b>Vitória Teixeira</b><span>Gerente Financeira · Medtec</span></div></figcaption>
      </figure>
      <figure class="quote reveal" data-d="1">
        <div class="quote__mark">"</div>
        <p>Grande eficiência e seriedade em soluções de comunicação, infraestrutura e outsourcing. Ágil e rápida.</p>
        <figcaption class="quote__who"><div class="quote__av">OS</div><div><b>Osmar Silva</b><span>Supervisor de TI · Kadão</span></div></figcaption>
      </figure>
    </div>
  </div>
</section>

{cta_band("Mapeamos seus fornecedores atuais sem compromisso",
          "Mostramos o que dá para centralizar, o que faz sentido manter e onde está o retrabalho da sua equipe.",
          "Quero o mapeamento gratuito")}
</main>
"""


# ===========================================================================
# CONTATO
# ===========================================================================
BODY_CONTATO = f"""
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <div class="page-hero__grid">
      <div>
        <span class="eyebrow">Fale com a Wicorp</span>
        <h1 class="display">Vamos entender sua <span class="grad-text">operação</span></h1>
        <p class="lead">Conte o que está acontecendo hoje e um especialista retorna em até 1 dia útil.
        Se preferir resolver agora, ligue ou chame no WhatsApp.</p>

        <div class="grid" style="gap:18px; margin-top:34px">
          <div class="feat">
            <div class="feat__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg></div>
            <div><h3>Comercial</h3><p><a href="tel:{TEL_HREF}" style="color:var(--w-teal)">{TEL}</a> · <a href="https://wa.me/{WPP_HREF}" data-pos="contato" target="_blank" rel="noopener" style="color:var(--w-teal)">WhatsApp {WPP}</a></p></div>
          </div>
          <div class="feat">
            <div class="feat__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22 6 12 13 2 6"/></svg></div>
            <div><h3>E-mail</h3><p><a href="mailto:{MAIL}" style="color:var(--w-teal)">{MAIL}</a></p></div>
          </div>
          <div class="feat">
            <div class="feat__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div>
            <div><h3>Já é cliente?</h3><p>Abertura de chamado pelo portal de suporte: <a href="https://wicorp.desk.ms" target="_blank" rel="noopener" style="color:var(--w-teal)">wicorp.desk.ms</a></p></div>
          </div>
          <div class="feat">
            <div class="feat__ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
            <div><h3>Escritório</h3><p>Av. Luiz Dumont Villares, 2078 — CJ 78<br>Parada Inglesa, São Paulo — SP · 02239-000</p></div>
          </div>
        </div>
      </div>
      {form("contato", "geral", "Fale com um especialista",
            "Retornamos em até 1 dia útil com alguém que entende do seu cenário.",
            "Enviar mensagem")}
    </div>
  </div>
</section>

{proof_band()}
</main>
"""


# ===========================================================================
# OBRIGADO — destino de conversão. Dispara generate_lead no GA4.
# ===========================================================================
BODY_OBRIGADO = f"""
<main id="main">
<section class="page-hero" style="text-align:center; border-bottom:none; padding-bottom:100px">
  <div class="wrap" style="max-width:640px">
    <svg width="72" height="72" viewBox="0 0 24 24" fill="none" stroke="url(#wgradok)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="margin:0 auto 28px" aria-hidden="true">
      <defs><linearGradient id="wgradok" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="#5BBFC6"/><stop offset="100%" stop-color="#C7D86E"/></linearGradient></defs>
      <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>
    </svg>
    <h1 class="display" style="margin-bottom:18px">Recebemos sua solicitação</h1>
    <p class="lead" style="margin-bottom:32px">Um especialista da Wicorp entra em contato em até 1 dia útil.
    Se o assunto for urgente, fale agora no WhatsApp ou ligue direto para o comercial.</p>
    <div class="hero__actions" style="justify-content:center">
      <a href="https://wa.me/{WPP_HREF}" data-pos="obrigado" class="btn btn--primary" target="_blank" rel="noopener">Falar agora no WhatsApp</a>
      <a href="tel:{TEL_HREF}" class="btn btn--ghost">Ligar: {TEL}</a>
    </div>
  </div>
</section>

<section class="section section--alt section--tight">
  <div class="wrap">
    <div class="section-head center">
      <h2 class="display">Enquanto isso, conheça as soluções</h2>
    </div>
    <div class="grid grid--4">
      <a class="card" href="solucoes/link-dedicado-empresarial.html"><h3 style="font-size:1rem;margin-bottom:7px">Link dedicado e Link.Box</h3><p style="font-size:.86rem;color:var(--tx-3)">Conexão com backup automático 4G/5G</p></a>
      <a class="card" href="solucoes/pabx-virtual-nuvem.html"><h3 style="font-size:1rem;margin-bottom:7px">PABX virtual com IA</h3><p style="font-size:.86rem;color:var(--tx-3)">Telefonia e atendimento em nuvem</p></a>
      <a class="card" href="solucoes/firewall-sd-wan.html"><h3 style="font-size:1rem;margin-bottom:7px">Firewall e SD-WAN</h3><p style="font-size:.86rem;color:var(--tx-3)">Proteção de rede gerenciada</p></a>
      <a class="card" href="solucoes/infraestrutura-ti.html"><h3 style="font-size:1rem;margin-bottom:7px">Infraestrutura</h3><p style="font-size:.86rem;color:var(--tx-3)">Cabeamento, Wi-Fi e CFTV</p></a>
    </div>
  </div>
</section>
</main>
"""


# ===========================================================================
# GERAÇÃO DOS ARQUIVOS
# ===========================================================================
PAGES = [
    dict(path="solucoes/link-dedicado-empresarial.html", prefix=P, body=BODY_LINK, faq=FAQ_LINK,
         title="Link Dedicado Empresarial e Backup de Internet 4G/5G | Wicorp",
         desc="Link dedicado com IP fixo, banda garantida e redundância automática por dois chips 4G/5G. "
              "Monitoramento 24/7 e SLA. Consulte a disponibilidade no seu endereço.",
         canonical="solucoes/link-dedicado-empresarial"),

    dict(path="solucoes/pabx-virtual-nuvem.html", prefix=P, body=BODY_PABX, faq=FAQ_PABX,
         title="PABX Virtual em Nuvem, SIP Trunk e Contact Center | Wicorp",
         desc="PABX virtual, SIP Trunk e Contact Center em nuvem com recursos de IA. Integre ligações, ramais "
              "e WhatsApp, reduza custo de telefonia e ganhe controle. Simule seu plano.",
         canonical="solucoes/pabx-virtual-nuvem"),

    dict(path="solucoes/firewall-sd-wan.html", prefix=P, body=BODY_FW, faq=FAQ_FW,
         title="Firewall Corporativo, SD-WAN e Antivírus Gerenciado | Wicorp",
         desc="Firewall de próxima geração, SD-WAN e antivírus com MDR e SOC 24/7 para empresas. Proteção de "
              "rede e dados alinhada à LGPD. Solicite um diagnóstico de cibersegurança.",
         canonical="solucoes/firewall-sd-wan"),

    dict(path="solucoes/infraestrutura-ti.html", prefix=P, body=BODY_INFRA, faq=FAQ_INFRA,
         title="Infraestrutura de TI, Cabeamento Estruturado e Suporte | Wicorp",
         desc="Projetos de infraestrutura de TI, cabeamento estruturado, Wi-Fi corporativo, CFTV e suporte "
              "técnico especializado em São Paulo. Solicite uma avaliação da sua estrutura.",
         canonical="solucoes/infraestrutura-ti"),

    dict(path="lp/centralizar-fornecedores-ti.html", prefix=P, body=BODY_LP, lp=True,
         title="Centralize os fornecedores de TI da sua empresa | Wicorp",
         desc="Internet, telefonia, firewall e suporte com um único parceiro. Mapeamos seus fornecedores "
              "atuais sem compromisso e mostramos o que dá para centralizar.",
         canonical="lp/centralizar-fornecedores-ti"),

    dict(path="contato.html", prefix="", body=BODY_CONTATO, active="contato",
         title="Contato | Wicorp — Infraestrutura de TI e Telecom em São Paulo",
         desc="Fale com um especialista da Wicorp. Telefone (11) 4800-5000, WhatsApp e e-mail comercial. "
              "Retornamos em até 1 dia útil.",
         canonical="contato"),

    dict(path="obrigado.html", prefix="", body=BODY_OBRIGADO, noindex=True,
         title="Obrigado pelo contato | Wicorp",
         desc="Recebemos sua solicitação. Um especialista da Wicorp entra em contato em até 1 dia útil.",
         canonical="obrigado"),
]


# Blog e páginas institucionais
_outros = lambda slug: [x for x in paginas.POSTS if x["slug"] != slug][:2]
for _p in paginas.POSTS:
    PAGES.append(dict(
        path=f"blog/{_p['slug']}.html", prefix=P, body=paginas.post_body(_p, _outros(_p["slug"])),
        title=f"{_p['titulo']} | Blog Wicorp",
        desc=_p["desc"], canonical=f"blog/{_p['slug']}", artigo=_p,
    ))

PAGES.append(dict(
    path="blog/index.html", prefix=P, body=paginas.blog_index(),
    title="Blog | Wicorp — Conectividade, telefonia e segurança para empresas",
    desc="Conteúdo técnico sem jargão sobre link dedicado, PABX em nuvem, SD-WAN e "
         "segurança de rede, para quem decide sobre a infraestrutura da empresa.",
    canonical="blog",
))

PAGES.append(dict(
    path="quem-somos.html", prefix="", body=paginas.QUEM_SOMOS,
    title="Quem somos | Wicorp — 28 anos em TI e Telecom em São Paulo",
    desc="Desde 1998 transformando tecnologia em conexão estratégica. Mais de 800 clientes "
         "e 700 equipamentos em operação em São Paulo e Grande São Paulo.",
    canonical="quem-somos",
))

PAGES.append(dict(
    path="privacidade.html", prefix="", body=paginas.PRIVACIDADE,
    title="Política de Privacidade | Wicorp",
    desc="Como a Wicorp trata os dados pessoais coletados neste site, conforme a Lei Geral "
         "de Proteção de Dados.",
    canonical="privacidade", noindex=True,
))

PAGES.append(dict(
    path="calculadora-custo-downtime.html", prefix="", body=paginas.CALCULADORA,
    title="Calculadora: quanto custa uma hora de operação parada | Wicorp",
    desc="Calcule quanto a indisponibilidade de internet custa para sua empresa por mês e "
         "por ano. Sem cadastro — o cálculo roda no seu navegador.",
    canonical="calculadora-custo-downtime",
))

PAGES.append(dict(
    path="404.html", prefix="", body=paginas.NAO_ENCONTRADA,
    title="Página não encontrada | Wicorp",
    desc="A página que você procura não existe ou mudou de endereço.",
    canonical="404", noindex=True,
))


def main():
    for pg in PAGES:
        prefix = pg["prefix"]
        html = head(pg["title"], pg["desc"], pg["canonical"], prefix)

        if pg.get("noindex"):
            html = html.replace('<meta name="robots" content="index, follow">',
                                '<meta name="robots" content="noindex, follow">')
        if pg.get("artigo"):
            import json
            a = pg["artigo"]
            art = {"@context": "https://schema.org", "@type": "BlogPosting",
                   "headline": a["titulo"], "description": a["desc"],
                   "datePublished": a["data"], "dateModified": a["data"],
                   "author": {"@type": "Organization", "name": "Wicorp"},
                   "publisher": {"@type": "Organization", "name": "Wicorp",
                                 "url": SITE + "/"},
                   "mainEntityOfPage": f"{SITE}/{pg['canonical']}"}
            html = html.replace("</head>",
                f'<script type="application/ld+json">{json.dumps(art, ensure_ascii=False)}</script>\n</head>')
        if pg.get("faq"):
            html = html.replace("</head>", faq_schema(pg["faq"]) + "\n</head>")

        html += header_lp(prefix) if pg.get("lp") else header(prefix, pg.get("active", ""))
        html += pg["body"]
        html += footer(prefix, lp=pg.get("lp", False))

        out = ROOT / pg["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print("  gerado  %-46s %7s bytes" % (pg["path"], format(len(html), ",")))


if __name__ == "__main__":
    print("Gerando paginas do site Wicorp\n")
    main()
    print("\nConcluido. Rode build-preview.py para gerar visualizacoes.")
