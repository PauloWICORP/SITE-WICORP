# Site Wicorp

Site institucional da Wicorp — Conexões Inteligentes.
HTML, CSS e JavaScript puros. Sem framework, sem build obrigatório, sem banco de dados.

**Fase atual:** front-end. Back-end, formulários e segurança entram depois.

---

## Como abrir no GitHub Codespaces

1. No repositório, clique em **Code** → aba **Codespaces** → **Create codespace on main**
2. Aguarde o ambiente subir (leva 1–2 minutos na primeira vez)
3. O servidor sobe sozinho na porta **8080** e o preview abre automaticamente

Se o preview não abrir, vá na aba **PORTS** do terminal e clique no ícone de globo
na porta 8080.

Para reiniciar o servidor manualmente:

```bash
python3 -m http.server 8080
```

---

## Como rodar na sua máquina

```bash
git clone https://github.com/SEU-USUARIO/wicorp-site.git
cd wicorp-site
python3 -m http.server 8000
```

Acesse `http://localhost:8000`.

---

## Estrutura

```
.
├── index.html                              Home
├── contato.html
├── obrigado.html                           Destino de conversão (dispara generate_lead)
├── solucoes/
│   ├── link-dedicado-empresarial.html
│   ├── pabx-virtual-nuvem.html
│   ├── firewall-sd-wan.html
│   └── infraestrutura-ti.html
├── lp/
│   └── centralizar-fornecedores-ti.html    Landing page de centralização
│
├── css/style.css                           Design system inteiro
├── js/main.js                              Interações + camada de rastreamento
├── img/
│   ├── logo-wicorp.png                     Versão negativa — usada no site
│   ├── logo-wicorp-original.png            Cores originais — fundo claro
│   └── favicon.png
│
├── build.py                                Gera as páginas internas
├── build-preview.py                        Gera HTML único para visualização
└── sections.py                             Seções visuais e interativas da home
```

### Um detalhe importante sobre os arquivos

O `index.html` é editado à mão. As **demais páginas são geradas** pelo `build.py`,
que concentra header, rodapé e `<head>` em um lugar só.

Se você editar `solucoes/pabx-virtual-nuvem.html` direto, a alteração **se perde**
no próximo `python3 build.py`. Para mudar uma página interna, edite o conteúdo dela
dentro de `build.py` e rode:

```bash
python3 build.py
```

O resultado continua sendo HTML estático puro — o script só evita ter que repetir
o mesmo menu em oito arquivos.

---

## Convenções que o projeto segue

Estas regras vêm do Pacote de Correção do Site e não são estética — são conversão.

| Regra | Por quê |
|---|---|
| Nenhum CTA genérico ("Saiba Mais", "Leia mais") | O Google usa o texto do link para entender o destino |
| Todo formulário tem 4 campos: nome, e-mail, empresa, WhatsApp | CNPJ antes da primeira conversa derruba a taxa de envio |
| Formulário sempre acima da dobra | Era a causa raiz dos "0 leads do site" |
| H1 com palavra-chave, subtítulo com benefício | Atende busca sem violar o Manual de Copy |
| Copy em Contexto → Consciência → Educação → Autoridade → Ação | Estrutura obrigatória do Manual de Copy |
| Sem banco de imagens | Mockups de produto em HTML/CSS, como faz a referência do setor |

### Paleta e tipografia

Do Manual de Identidade Visual:

```
#5BBFC6   #63A9BF   #74BE9A   #ADD189   #C7D86E
```

Títulos em **Bebas Neue**, corpo em **Roboto**.

Todas as cores vivem como variáveis CSS no topo de `css/style.css`.
Mudar lá muda o site inteiro.

---

## Rastreamento

O `js/main.js` já empurra os eventos para o `dataLayer`, prontos para o GTM
criar as tags. Nenhum código de GTM está instalado ainda.

| Evento | Quando dispara |
|---|---|
| `generate_lead` | Formulário enviado — **conversão principal** |
| `form_start` | Primeiro campo recebe foco (mede abandono) |
| `click_whatsapp` | Clique em qualquer link do WhatsApp |
| `click_telefone` | Clique em link `tel:` |
| `view_solucao` | Troca de aba na home |
| `simulou_failover` | Uso do simulador do Link.Box |
| `scroll_90` | 90% da página lida |

---

## O que falta

- [ ] Endpoint do formulário e integração com o funil de entrada do Piperun
- [ ] Instalar o GTM e marcar os eventos como principais no GA4
- [ ] Fotos autorais: hardware do Link.Box, NOC 24/7, equipe em campo
- [ ] Blog
- [ ] Levar as abas e o simulador para as páginas internas
- [ ] Publicação e redirects 301 do domínio antigo

---

## Publicação

Site estático roda em qualquer lugar. As opções gratuitas que aceitam deploy
direto do GitHub:

- **Cloudflare Pages** — conecta o repositório, sem comando de build
- **Netlify** — arrasta a pasta ou conecta o repositório
- **Vercel** — conecta o repositório
- **GitHub Pages** — Settings → Pages → branch `main`

Em todas: sem PHP, sem banco, sem painel administrativo. Nada para invadir.
