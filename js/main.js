/* ==========================================================================
   WICORP — main.js
   Interações do site + camada de rastreamento.

   Os eventos disparados aqui seguem exatamente o plano de rastreamento
   definido no Pacote de Correção do Site (seção 07):
     generate_lead   → conversão principal
     form_start      → mede abandono de formulário
     click_whatsapp  → conversão secundária
     click_telefone  → conversão secundária
     view_precos     → sinal de intenção
     scroll_90       → qualidade de leitura
   Todos vão para o dataLayer, prontos para o GTM criar as tags.
   ========================================================================== */
(function () {
  'use strict';

  window.dataLayer = window.dataLayer || [];

  /** Envia evento para o dataLayer (GTM). */
  function track(event, params) {
    var payload = Object.assign({ event: event, page_path: location.pathname }, params || {});
    window.dataLayer.push(payload);
    if (window.WICORP_DEBUG) console.log('[track]', payload);
  }

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ----------------------------------------------------------------------
     1. Header — fundo sólido ao rolar
     ---------------------------------------------------------------------- */
  var header = $('.header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 20);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ----------------------------------------------------------------------
     2. Menu mobile
     ---------------------------------------------------------------------- */
  var burger = $('.burger');
  var mobile = $('.mobile-menu');
  if (burger && mobile) {
    var toggleMenu = function (open) {
      var isOpen = open !== undefined ? open : burger.getAttribute('aria-expanded') !== 'true';
      burger.setAttribute('aria-expanded', String(isOpen));
      mobile.classList.toggle('is-open', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    };
    burger.addEventListener('click', function () { toggleMenu(); });
    $$('a', mobile).forEach(function (a) {
      a.addEventListener('click', function () { toggleMenu(false); });
    });
    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') toggleMenu(false);
    });
  }

  /* ----------------------------------------------------------------------
     3. Animação de entrada ao rolar
     ---------------------------------------------------------------------- */
  var reveals = $$('.reveal');
  if (reveals.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            en.target.classList.add('is-in');
            io.unobserve(en.target);
          }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      reveals.forEach(function (el) { io.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add('is-in'); });
    }
  }

  /* ----------------------------------------------------------------------
     4. Contadores da barra de prova social
     ---------------------------------------------------------------------- */
  var counters = $$('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        cio.unobserve(el);
        var target = parseInt(el.getAttribute('data-count'), 10);
        var suffix = el.getAttribute('data-suffix') || '';
        var prefix = el.getAttribute('data-prefix') || '';
        var dur = 1100, t0 = null;
        var step = function (ts) {
          if (!t0) t0 = ts;
          var p = Math.min((ts - t0) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = prefix + Math.round(target * eased).toLocaleString('pt-BR') + suffix;
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ----------------------------------------------------------------------
     5. Formulários — validação + eventos
     ---------------------------------------------------------------------- */
  var reEmail = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  /** Descarta e-mails pessoais: o público é B2B. */
  var freeDomains = ['gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com', 'yahoo.com.br',
                     'bol.com.br', 'uol.com.br', 'live.com', 'icloud.com', 'terra.com.br'];

  function setError(field, msg) {
    field.classList.add('has-error');
    var box = $('.field__err', field);
    if (box) box.textContent = msg;
  }
  function clearError(field) {
    field.classList.remove('has-error');
  }

  function validate(input) {
    var field = input.closest('.field');
    if (!field) return true;
    var val = input.value.trim();
    var name = input.name;

    if (input.required && !val) {
      setError(field, 'Campo obrigatório.');
      return false;
    }
    if (name === 'email') {
      if (!reEmail.test(val)) {
        setError(field, 'Informe um e-mail válido.');
        return false;
      }
      var dom = val.split('@')[1].toLowerCase();
      if (freeDomains.indexOf(dom) !== -1) {
        setError(field, 'Use o e-mail corporativo da sua empresa.');
        return false;
      }
    }
    if (name === 'whatsapp') {
      var digits = val.replace(/\D/g, '');
      if (digits.length < 10 || digits.length > 11) {
        setError(field, 'Informe DDD + número.');
        return false;
      }
    }
    if (name === 'nome' && val.length < 3) {
      setError(field, 'Informe seu nome.');
      return false;
    }
    clearError(field);
    return true;
  }

  /** Máscara de telefone brasileiro. */
  function maskPhone(v) {
    var d = v.replace(/\D/g, '').slice(0, 11);
    if (d.length <= 2)  return d.length ? '(' + d : '';
    if (d.length <= 6)  return '(' + d.slice(0, 2) + ') ' + d.slice(2);
    if (d.length <= 10) return '(' + d.slice(0, 2) + ') ' + d.slice(2, 6) + '-' + d.slice(6);
    return '(' + d.slice(0, 2) + ') ' + d.slice(2, 7) + '-' + d.slice(7);
  }

  $$('form[data-wicorp-form]').forEach(function (form) {
    var card    = form.closest('.form-card');
    var formId  = form.getAttribute('data-form-id') || 'form';
    var solucao = form.getAttribute('data-solucao') || 'geral';
    var started = false;

    // form_start — dispara uma única vez, no primeiro foco
    form.addEventListener('focusin', function () {
      if (started) return;
      started = true;
      track('form_start', { form_id: formId, solucao: solucao });
    });

    // Máscara e validação em tempo real
    $$('input', form).forEach(function (input) {
      if (input.name === 'whatsapp') {
        input.addEventListener('input', function () {
          var pos = input.selectionStart === input.value.length;
          input.value = maskPhone(input.value);
          if (pos) input.setSelectionRange(input.value.length, input.value.length);
        });
      }
      input.addEventListener('blur', function () {
        if (input.value.trim()) validate(input);
      });
      input.addEventListener('input', function () {
        var f = input.closest('.field');
        if (f && f.classList.contains('has-error')) clearError(f);
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var ok = true;
      $$('input[required], textarea[required]', form).forEach(function (input) {
        if (!validate(input)) ok = false;
      });
      if (!ok) {
        var firstErr = $('.field.has-error input', form);
        if (firstErr) firstErr.focus();
        return;
      }

      var btn = $('button[type="submit"]', form);
      if (btn) { btn.disabled = true; btn.textContent = 'Enviando...'; }

      // generate_lead — CONVERSÃO PRINCIPAL do plano de rastreamento
      track('generate_lead', {
        form_id: formId,
        solucao: solucao,
        origem: document.referrer || 'direct'
      });

      // ------------------------------------------------------------------
      // Nesta fase o site é só visual — não há backend.
      // Quando o back entrar, é aqui que o POST vai (endpoint + Piperun).
      // ------------------------------------------------------------------
      setTimeout(function () {
        if (card) {
          card.classList.add('is-sent');
          card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        form.reset();
        if (btn) { btn.disabled = false; btn.textContent = btn.getAttribute('data-label') || 'Enviar'; }
      }, 600);
    });
  });

  /* ----------------------------------------------------------------------
     6. Cliques em WhatsApp e telefone
     ---------------------------------------------------------------------- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a');
    if (!a || !a.href) return;

    if (a.href.indexOf('wa.me') !== -1 || a.href.indexOf('api.whatsapp') !== -1) {
      track('click_whatsapp', { posicao: a.getAttribute('data-pos') || 'nao-definido' });
    } else if (a.href.indexOf('tel:') === 0) {
      track('click_telefone', { numero: a.href.replace('tel:', '') });
    }
  });

  /* ----------------------------------------------------------------------
     7. view_precos — bloco de planos 50% visível
     ---------------------------------------------------------------------- */
  var precos = $('[data-precos]');
  if (precos && 'IntersectionObserver' in window) {
    var pio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          track('view_precos', { solucao: precos.getAttribute('data-precos') });
          pio.disconnect();
        }
      });
    }, { threshold: 0.5 });
    pio.observe(precos);
  }

  /* ----------------------------------------------------------------------
     8. scroll_90 — leitura da página
     ---------------------------------------------------------------------- */
  var fired90 = false;
  window.addEventListener('scroll', function () {
    if (fired90) return;
    var h = document.documentElement;
    var pct = (h.scrollTop + window.innerHeight) / h.scrollHeight;
    if (pct >= 0.9) {
      fired90 = true;
      track('scroll_90');
    }
  }, { passive: true });

  /* ----------------------------------------------------------------------
     9. Ano corrente no rodapé
     ---------------------------------------------------------------------- */
  $$('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });


  /* ----------------------------------------------------------------------
     10. ABAS DE SOLUÇÃO — troca o mockup ao clicar
     ---------------------------------------------------------------------- */
  var tabs = $$('.tab[role="tab"]');
  if (tabs.length) {
    function selectTab(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) {
          panel.hidden = !on;
          panel.classList.toggle('is-on', on);
        }
      });
      if (focus) tab.focus();
      track('view_solucao', { solucao: tab.getAttribute('data-tab') });
    }

    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () { selectTab(tab); });
      // Navegação por teclado, como manda o padrão de tablist
      tab.addEventListener('keydown', function (e) {
        var i = tabs.indexOf(tab), n = null;
        if (e.key === 'ArrowDown' || e.key === 'ArrowRight') n = tabs[(i + 1) % tabs.length];
        else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') n = tabs[(i - 1 + tabs.length) % tabs.length];
        else if (e.key === 'Home') n = tabs[0];
        else if (e.key === 'End') n = tabs[tabs.length - 1];
        if (n) { e.preventDefault(); selectTab(n, true); }
      });
    });
  }

  /* ----------------------------------------------------------------------
     11. SIMULADOR DE FAILOVER DO LINK.BOX
     Reproduz a sequência real: fibra cai, NOC detecta, backup assume.
     ---------------------------------------------------------------------- */
  var failTrigger = $('[data-fail-trigger]');
  if (failTrigger) {
    var failReset  = $('[data-fail-reset]');
    var failLabel  = $('[data-fail-label]');
    var badge      = $('[data-fail-badge]');
    var badgeTxt   = $('[data-fail-badge-txt]');
    var uptime     = $('[data-fail-uptime]');
    var uptimeLbl  = $('[data-fail-uptime-lbl]');
    var logBox     = $('[data-fail-log]');
    var routes     = {};
    $$('[data-route]').forEach(function (r) { routes[r.getAttribute('data-route')] = r; });

    var timers = [];
    var running = false;

    function setRoute(key, state, meta, label) {
      var r = routes[key];
      if (!r) return;
      r.classList.remove('is-active', 'is-down', 'is-standby');
      if (state) r.classList.add(state);
      if (meta)  $('[data-route-meta]', r).textContent = meta;
      if (label) $('[data-route-state]', r).textContent = label;
    }

    function log(html) {
      var el = document.createElement('span');
      el.innerHTML = html;
      logBox.insertBefore(el, logBox.firstChild);
      while (logBox.children.length > 4) logBox.removeChild(logBox.lastChild);
    }

    function at(ms, fn) { timers.push(setTimeout(fn, ms)); }

    function restore() {
      timers.forEach(clearTimeout); timers = [];
      running = false;
      setRoute('fibra', 'is-active',  'Latência 8 ms · perda 0,0%',   'Ativo');
      setRoute('sim1',  'is-standby', 'Em espera · sinal −67 dBm',    'Standby');
      setRoute('sim2',  'is-standby', 'Em espera · sinal −72 dBm',    'Standby');
      badge.classList.remove('is-alert');
      badgeTxt.textContent = 'Operação conectada';
      uptime.textContent = '99,98%';
      uptimeLbl.textContent = 'disponibilidade no mês';
      logBox.innerHTML = '<span>NOC · monitoramento ativo em 3 rotas</span>';
      failLabel.textContent = 'Simular queda do link';
      failTrigger.disabled = false;
      failReset.disabled = true;
    }

    function simulate() {
      if (running) return;
      running = true;
      failTrigger.disabled = true;
      failReset.disabled = false;
      failLabel.textContent = 'Simulando...';
      track('simulou_failover', {});

      // t=0 — a fibra cai
      setRoute('fibra', 'is-down', 'Sem resposta · perda 100%', 'Queda');
      badge.classList.add('is-alert');
      badgeTxt.textContent = 'Falha detectada na fibra';
      uptime.textContent = '0,0s';
      uptimeLbl.textContent = 'tempo sem conexão';
      log('<i>ALERTA</i> · perda de sinal na fibra dedicada');

      // t=0,4s — o Link.Box confirma a queda
      at(400, function () {
        log('Link.Box · confirmando a falha em 3 tentativas');
        uptime.textContent = '0,4s';
      });

      // t=1,1s — o 5G assume
      at(1100, function () {
        setRoute('sim1', 'is-active', 'Assumindo tráfego · sinal −67 dBm', 'Ativo');
        badgeTxt.textContent = 'Comutando para o backup 5G';
        uptime.textContent = '1,1s';
        log('<b>COMUTADO</b> · tráfego migrado para o 5G da operadora A');
      });

      // t=1,8s — o 4G entra como segunda camada
      at(1800, function () {
        setRoute('sim2', 'is-standby', 'Pronto como segunda rota · −72 dBm', 'Reserva');
        log('Backup 4G · pronto como segunda camada de contingência');
      });

      // t=2,4s — operação normalizada, ninguém precisou agir
      at(2400, function () {
        badge.classList.remove('is-alert');
        badgeTxt.textContent = 'Operação seguiu conectada';
        uptime.textContent = '1,1s';
        uptimeLbl.textContent = 'tempo total sem conexão';
        log('<b>OK</b> · operação normalizada sem intervenção da equipe');
        failLabel.textContent = 'Simular novamente';
        failTrigger.disabled = false;
        running = false;
      });
    }

    failTrigger.addEventListener('click', simulate);
    failReset.addEventListener('click', restore);
  }

  /* ----------------------------------------------------------------------
     12. CARROSSEL
     ---------------------------------------------------------------------- */
  $$('[data-carousel]').forEach(function (car) {
    var track  = $('.carousel__track', car);
    var slides = $$('.carousel__slide', car);
    var prev   = $('[data-car-prev]', car);
    var next   = $('[data-car-next]', car);
    var dotBox = $('.carousel__dots', car);
    var idx = 0;

    function perView() { return window.innerWidth <= 760 ? 1 : 2; }
    function maxIdx()  { return Math.max(0, slides.length - perView()); }

    function render() {
      var slide = slides[0].getBoundingClientRect().width;
      var gap = parseFloat(getComputedStyle(track).gap) || 22;
      track.style.transform = 'translateX(' + (-idx * (slide + gap)) + 'px)';
      if (prev) prev.disabled = idx === 0;
      if (next) next.disabled = idx >= maxIdx();
      $$('.carousel__dot', dotBox).forEach(function (d, i) {
        d.classList.toggle('is-on', i === idx);
      });
    }

    if (dotBox) {
      for (var i = 0; i <= maxIdx(); i++) {
        var d = document.createElement('button');
        d.className = 'carousel__dot';
        d.setAttribute('aria-label', 'Ir para o depoimento ' + (i + 1));
        (function (n) { d.addEventListener('click', function () { idx = n; render(); }); })(i);
        dotBox.appendChild(d);
      }
    }
    if (prev) prev.addEventListener('click', function () { idx = Math.max(0, idx - 1); render(); });
    if (next) next.addEventListener('click', function () { idx = Math.min(maxIdx(), idx + 1); render(); });

    var rt;
    window.addEventListener('resize', function () {
      clearTimeout(rt);
      rt = setTimeout(function () { idx = Math.min(idx, maxIdx()); render(); }, 150);
    });
    render();
  });

})();
