# Site Wicorp

Site institucional da Wicorp — Conexões Inteligentes.
HTML, CSS e JavaScript puros. Sem framework, sem build obrigatório, sem banco de dados.

**Fase atual:** front-end concluído — 19 páginas, no ar em preview pelo GitHub Pages:
https://paulowicorp.github.io/SITE-WICORP/ (todo `git push` atualiza o link sozinho).
Back-end, formulários e segurança entram na fase seguinte.

---

## Como abrir no GitHub Codespaces

1. No repositório, clique em **Code** → aba **Codespaces** → **Create codespace on main**
2. Aguarde o ambiente subir (1–2 minutos na primeira vez)
3. O servidor sobe sozinho na porta **8080** e o preview abre automaticamente

Se o preview não abrir, vá na aba **PORTS** e clique no ícone de globo na porta 8080.

Para subir o servidor manualmente sem prender o terminal:

```bash
nohup python3 -m http.server 8080 > /tmp/servidor.log 2>&1 &
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

## As 19 páginas

```
.
├── index.html                                Home
├── quem-somos.html                           Autoridade: 28 anos, NOC, equipe própria
├── contato.html
├── obrigado.html                             Destino de conversão
├── suporte.html                              Canais de suporte para quem já é cliente
├── privacidade.html                          Política de Privacidade / LGPD
├── 404.html                                  Página não encontrada
│
├── consulta-disponibilidade.html             Consulta de CEP → viabilidade de link
├── calculadora-custo-downtime.html           Calculadora de custo de queda
│
├── solucoes/
│   ├── link-dedicado-empresarial.html        A CONEXÃO (fibra ou rádio, banda garantida)
│   ├── link-box-redundancia.html             O EQUIPAMENTO (multi-link + 2 chips 4G/5G)
│   ├── pabx-virtual-nuvem.html
│   ├── firewall-sd-wan.html
│   └── infraestrutura-ti.html
│
├── blog/
│   ├── index.html
│   ├── pabx-em-nuvem-vale-a-pena.html
│   ├── link-box-redundancia-internet.html
│   └── sd-wan-reduzir-custo-link.html
│
└── lp/
    └── centralizar-fornecedores-ti.html      Landing page de centralização
```

> **Link dedicado e Link.Box são produtos diferentes e têm páginas separadas.**
> Link dedicado é a conexão. Link.Box é o equipamento que gerencia vários links e
> comuta para dois chips 4G/5G — funciona inclusive sobre link de outra operadora.

---

## Arquivos de apoio

```
css/style.css          Design system inteiro (42 seções numeradas)
js/main.js             Interações + camada de rastreamento (15 blocos numerados)
img/logo-wicorp.png    Versão negativa — usada no site
img/logo-wicorp-original.png
img/favicon.png
img/fotos/             Fotos reais: NOC, racks, escritório, Link.Box
img/arte/              Imagens de apoio e texturas
img/logos/             Logos de clientes nos depoimentos (ver LEIA-ME.txt)
build.py               Gera todas as páginas, menos a index
build-preview.py       Gera HTML único com CSS e JS embutidos
sections.py            Seções visuais e interativas
paginas.py             Blog, quem somos, privacidade, calculadora, consulta de CEP, suporte
conectividade.py       Páginas de link dedicado e Link.Box
```

### Um detalhe importante sobre os arquivos

O `index.html` é editado à mão. As **demais páginas são geradas** pelo `build.py`,
que concentra header, rodapé e `<head>` em um lugar só.

Se você editar `solucoes/pabx-virtual-nuvem.html` direto, a alteração **se perde**
no próximo `python3 build.py`. Para mudar uma página interna, edite o conteúdo dela
dentro de `build.py` (ou de `paginas.py` / `conectividade.py`) e rode:

```bash
python3 build.py
```

O resultado continua sendo HTML estático puro — o script só evita repetir o mesmo
menu em dezenove arquivos.

---

## Recursos interativos

| Onde | O quê |
|---|---|
| Home | Abas de soluções, simulador de failover, antes/depois, carrossel de depoimentos |
| Link.Box | Simulador de queda de link com comutação para 4G/5G |
| PABX virtual | Dimensionador de ramais (mostra configuração, não preço) |
| Calculadora | Custo de downtime por hora, a partir dos números da própria empresa |
| Consulta de CEP | Busca de endereço com liberação progressiva do formulário |

Nenhuma ferramenta exibe preço. Preço é conversa comercial, não número de site.

---

## Convenções que o projeto segue

Estas regras vêm do Pacote de Correção do Site e não são estética — são conversão.

| Regra | Por quê |
|---|---|
| Nenhum CTA genérico ("Saiba Mais", "Leia mais") | O Google usa o texto do link para entender o destino |
| Todo formulário tem 4 campos: nome, e-mail, empresa, WhatsApp | CNPJ antes da primeira conversa derruba a taxa de envio |
| Formulário sempre acima da dobra | Era a causa raiz dos "0 leads do site" |
| E-mail gratuito é recusado no formulário | Lead B2B qualificado usa e-mail corporativo |
| H1 com palavra-chave, subtítulo com benefício | Atende busca sem violar o Manual de Copy |
| Copy em Contexto → Consciência → Educação → Autoridade → Ação | Estrutura obrigatória do Manual de Copy |
| Imagens em `<picture>` com WebP + fallback e `aspect-ratio` fixo | Peso menor e zero salto de layout |

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

O `js/main.js` já empurra os eventos para o `dataLayer`, prontos para o GTM criar
as tags. **Nenhum código de GTM está instalado ainda** — isso é da fase seguinte.

| Evento | Quando dispara |
|---|---|
| `generate_lead` | Formulário enviado — **conversão principal** |
| `form_start` | Primeiro campo recebe foco (mede abandono) |
| `consulta_cep` | CEP consultado na página de disponibilidade |
| `click_whatsapp` | Clique em qualquer link do WhatsApp |
| `click_telefone` | Clique em link `tel:` |
| `view_solucao` | Troca de aba na home |
| `view_precos` | Seção de investimento entra na tela |
| `simulou_failover` | Uso do simulador do Link.Box |
| `dimensionou_ramais` | Uso do dimensionador de ramais |
| `calculou_downtime` | Uso da calculadora de custo de queda |
| `scroll_90` | 90% da página lida |

---

## O que falta (fora desta fase)

- [ ] Endpoint do formulário e integração com o funil de entrada do Piperun
- [ ] Instalar o GTM e marcar `generate_lead` como conversão principal no GA4
- [ ] Revisão jurídica da Política de Privacidade — os campos `[a definir]`
      (CNPJ, prazo de retenção, encarregado de dados) precisam ser preenchidos
- [ ] Fotos de técnico em campo — única lacuna do banco de imagens
- [ ] Logos dos clientes nos depoimentos, após autorização de cada um
- [ ] 3 landing pages restantes — recomendo só quando a mídia paga começar
- [ ] Publicação, redirects 301 do domínio antigo e limpeza do spam de SEO
      injetado no WordPress atual

---

## Depoimentos e logos de clientes

Cada depoimento tem uma placa com o nome da empresa, no canto superior do card.
Essa placa é o lugar da logo. Enquanto a autorização do cliente não sai, ela mostra
o nome em texto; quando o arquivo chegar, troque

```html
<div class="quote__logo"><span>Medtec</span></div>
```

por

```html
<div class="quote__logo"><img src="img/logos/medtec.png" alt="Medtec"></div>
```

O CSS já limita altura e largura. Detalhes em `img/logos/LEIA-ME.txt`.

**Usar logo de cliente exige autorização dele.** Depoimento assinado não implica
permissão de uso de marca — são coisas separadas.

---

## Publicação

Site estático roda em qualquer lugar. As opções gratuitas com deploy direto do GitHub:

- **Cloudflare Pages** — conecta o repositório, sem comando de build
- **Netlify** — arrasta a pasta ou conecta o repositório
- **Vercel** — conecta o repositório
- **GitHub Pages** — Settings → Pages → branch `main`

Para mostrar rápido ao time de marketing, sem mexer em domínio:
`app.netlify.com/drop` → arraste a pasta do projeto → sai uma URL temporária.

Em todas: sem PHP, sem banco, sem painel administrativo. Nada para invadir.
