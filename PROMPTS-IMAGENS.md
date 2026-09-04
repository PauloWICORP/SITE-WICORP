# Prompts para gerar imagens do site Wicorp

Cole cada prompt no gerador (Midjourney, DALL·E, Firefly, Gemini, o que você usar).
Mande o resultado que eu otimizo e coloco no site.

---

## Antes de tudo: onde IA ajuda e onde atrapalha

**Não peça IA para gerar:** NOC, equipe, rack instalado, Link.Box, escritório.
Você já tem foto real de tudo isso — e imagem gerada imitando essas coisas seria
exatamente o erro que o diagnóstico da Gonçalves Rauber apontou nos criativos atuais:
*"acervos fotográficos comerciais de modelos em situações ilustrativas, omitindo os
ativos tecnológicos proprietários da companhia"*. Trocar foto de banco por foto de IA
não corrige nada.

**Peça IA para gerar:** fundo abstrato, textura, capa conceitual de artigo e imagem de
compartilhamento. São elementos decorativos — ninguém olha e pensa que é a Wicorp
de verdade. É aí que a IA é honesta e útil.

---

## Referência de marca — vale colar junto em qualquer prompt

```
Paleta: #5BBFC6 (teal) · #63A9BF (azul) · #74BE9A (verde)
        #ADD189 (sage) · #C7D86E (lima)
Fundo:  #080C0E (quase preto) e #0E1417
Estilo: escuro, técnico, sóbrio, corporativo — nada de neon exagerado
```

**Negativo em todos** (o que NÃO pode aparecer):

```
no text, no words, no letters, no logos, no watermarks, no UI mockups,
no people, no faces, no hands, no stock photo look, no cliché
"digital transformation" imagery, no glowing blue businessman,
no world map with connection lines
```

---

## 1. Imagem de compartilhamento (Open Graph) — **a mais importante**

O site não tem nenhuma. É a imagem que aparece quando alguém compartilha um link
da Wicorp no WhatsApp, LinkedIn ou Slack. Hoje aparece um retângulo vazio.

**Formato:** 1200 × 630 px

```
Abstract dark technology background for a corporate telecom company.
Deep near-black background (#080C0E) with soft flowing gradient ribbons
in teal (#5BBFC6), green (#74BE9A) and lime (#C7D86E), curving from the
lower left toward the upper right. Subtle fiber-optic light strands,
very thin, out of focus in the background. Large empty negative space
in the left two thirds for text overlay. Cinematic, restrained,
premium enterprise feel. Not busy. Not neon.
```

---

## 2. Capas dos três artigos do blog

Hoje cada card usa um ícone vetorial sobre gradiente. Funciona, mas uma capa
conceitual dá mais presença na listagem e no compartilhamento.

**Formato:** 1600 × 900 px (16:9)

### 2a. PABX em nuvem

```
Abstract visualization of cloud telephony. Dark near-black background.
Soft translucent geometric shapes suggesting sound waves and conversation
flow, rendered in teal and soft green gradients. Thin curved lines
connecting floating rounded nodes, like voice paths converging into one
point. Minimal, calm, lots of empty space. Corporate, not playful.
```

### 2b. Link.Box e redundância

```
Abstract visualization of network redundancy. Dark near-black background.
One bright continuous light path in teal breaks and fades midway, while
two alternative light paths in green and lime immediately illuminate and
carry the flow forward. Sense of automatic rerouting and continuity.
Minimal geometric style, thin lines, soft glow, generous empty space.
```

### 2c. SD-WAN e custo de link

```
Abstract visualization of intelligent network traffic distribution.
Dark near-black background. Multiple parallel light channels in teal,
green and lime, with varying thickness suggesting different priority
levels and bandwidth. Streams merging and separating cleanly.
Orderly, technical, calm. Thin lines, soft glow, plenty of dark space.
```

---

## 3. Texturas de fundo para seções

Usadas por baixo do conteúdo, com bastante transparência. Precisam ser
**muito discretas** — se competirem com o texto, não servem.

**Formato:** 1920 × 1080 px

### 3a. Textura de fibra óptica

```
Extremely subtle abstract texture. Near-black background (#0A1013).
Very faint fiber optic filaments crossing diagonally, barely visible,
in dark teal and dark green. Low contrast, low brightness, no focal point.
Designed to sit behind white text at 15% opacity. Almost imperceptible.
```

### 3b. Malha de rede

```
Extremely subtle abstract network mesh texture. Near-black background.
Sparse thin connecting lines and tiny nodes forming an irregular
constellation, in very dark teal. Extremely low contrast, evenly
distributed, no focal point. Background texture only, not a
foreground graphic.
```

---

## 4. Ilustração de centralização de fornecedores — **opcional, mas boa**

Para a landing page de centralização. É o conceito central do posicionamento
de vocês e hoje está só em diagrama CSS.

**Formato:** 1400 × 1000 px

```
Abstract conceptual illustration, dark near-black background.
Left side: five scattered, disconnected nodes in dull gray, tangled
irregular lines between them, visual sense of disorder.
Right side: the same five nodes organized around one central hub,
connected by clean curved lines in teal and lime gradient.
Clear before-and-after contrast. Flat geometric style, no text,
no icons, no people. Calm and corporate.
```

---

## Como mandar de volta

- **PNG ou JPG na maior resolução** que o gerador entregar — eu redimensiono
- Diga qual prompt gerou qual arquivo, ou nomeie: `og.png`, `blog-pabx.png`, etc.
- Se vier com fundo branco quando devia ser escuro, me avise que eu ajusto

Se algum resultado não ficar bom, me manda mesmo assim e eu digo o que mudar no
prompt — geralmente é questão de tirar palavra que o gerador interpreta como
"encha de elemento".

---

## O que já está resolvido com foto real

Não precisa gerar nada para estes — as fotos que você mandou cobrem:

| Uso | Foto |
|---|---|
| NOC em operação | `noc-equipe`, `noc-sala` |
| Rack e cabeamento | `rack`, `rack-cliente` |
| Link.Box | `link-box`, `link-box-mesa` |
| Escritório e equipe | `escritorio` |
| Recepção com a marca | `recepcao` |
