# Painel de conteúdo — instalação no servidor

O painel roda no servidor Linux de vocês. Ele é a **única** parte do projeto
que executa código. O site em si continua sendo arquivo estático: HTML, CSS,
JS e imagem. Se o painel for desligado, o site continua no ar exatamente como
estava — isso é proposital.

---

## 1. Dependências

```bash
cd /caminho/do/site
python3 -m venv .venv
source .venv/bin/activate
pip install -r painel/requisitos.txt
```

Python 3.9 ou mais novo. São duas bibliotecas: Flask e Pillow.

## 2. Criar a senha

```bash
python3 painel/criar-senha.py
```

Ele pede usuário e senha e grava `painel/config.json` com permissão `600`.
**A senha não é guardada** — só o hash (scrypt). Se esquecer, rode de novo.

Use no mínimo 12 caracteres. Esse painel escreve no site publicado.

## 3. Testar

```bash
python3 painel/app.py
```

Abra `http://127.0.0.1:8090/admin`. Crie uma novidade de teste, confira se ela
aparece no site e remova.

## 4. Deixar rodando (systemd)

`/etc/systemd/system/wicorp-painel.service`:

```ini
[Unit]
Description=Painel de conteudo Wicorp
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/caminho/do/site
Environment="PAINEL_HTTPS=1"
ExecStart=/caminho/do/site/.venv/bin/python painel/app.py
Restart=always
RestartSec=5

# O painel só precisa escrever no próprio projeto
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ReadWritePaths=/caminho/do/site

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now wicorp-painel
sudo systemctl status wicorp-painel
```

`ExecStart` precisa ser o Python do venv, não o do sistema.

## 5. nginx na frente

O nginx entrega o site estático — que é o que 99% das visitas pedem — e só
encaminha `/admin` para o painel.

```nginx
server {
    listen 443 ssl http2;
    server_name wicorp.com.br www.wicorp.com.br;

    ssl_certificate     /etc/letsencrypt/live/wicorp.com.br/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/wicorp.com.br/privkey.pem;

    root /caminho/do/site;
    index index.html;

    # O site: arquivo puro, sem passar por Python
    location / {
        try_files $uri $uri/ =404;
    }
    error_page 404 /404.html;

    # Nada de servir código-fonte nem configuração
    location ~ ^/(painel|\.git)/ { deny all; return 404; }
    location ~ \.(py|json|md)$   { deny all; return 404; }

    # Exceção: as imagens das novidades são conteúdo, não código
    location /img/ { try_files $uri =404; }

    # O painel
    location /admin {
        proxy_pass http://127.0.0.1:8090;
        proxy_set_header Host              $host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        client_max_body_size 10M;   # precisa ser maior que o limite do painel
    }
}

server {
    listen 80;
    server_name wicorp.com.br www.wicorp.com.br;
    return 301 https://$host$request_uri;
}
```

`client_max_body_size` menor que 10M faz upload de imagem falhar com erro do
nginx antes de chegar ao painel — é o motivo mais comum de "não sobe a foto".

### Restringir o /admin à rede interna (recomendado)

Como o servidor é interno, dá para exigir que o painel só responda de dentro:

```nginx
location /admin {
    allow 192.168.0.0/16;    # ajuste para a faixa de vocês
    allow 10.0.0.0/8;
    deny all;
    proxy_pass http://127.0.0.1:8090;
    # ... os mesmos proxy_set_header acima
}
```

Isso reduz a superfície de ataque a praticamente zero: de fora da rede, o
`/admin` nem existe.

## 6. Rebuild diário

Uma novidade com data final sai do ar sozinha no navegador — o JS confere a
data. Mas o HTML só é regerado quando alguém publica. Para o servidor também
ficar correto, rode o build uma vez por dia:

```bash
sudo crontab -e
```

```cron
5 3 * * * cd /caminho/do/site && .venv/bin/python build.py >> /var/log/wicorp-build.log 2>&1
```

## 7. Atualizações de código

O GitHub continua sendo o repositório. O fluxo fica assim:

```bash
cd /caminho/do/site
git pull
.venv/bin/python build.py
```

**`conteudo.json` e `img/novidades/` não entram no Git** — são conteúdo,
escritos pelo painel no servidor. Já estão no `.gitignore` justamente para
que um `git pull` nunca apague uma novidade publicada.

---

## O que o painel faz para não virar porta de entrada

O site anterior foi invadido pelo WordPress. Um painel novo é superfície de
ataque nova, então estas decisões são deliberadas:

| Decisão | Motivo |
|---|---|
| Senha com scrypt e sal aleatório | Vazamento do arquivo não entrega a senha |
| Máximo de 5 tentativas por IP a cada 15 min | Elimina ataque de força bruta |
| Token anti-CSRF em todo formulário | Impede que outro site dispare ações em nome de quem está logado |
| Imagem reaberta e reescrita pelo Pillow | O arquivo que vai para o disco é gerado aqui, não o que o navegador mandou |
| Nome de arquivo gerado pelo servidor | O nome original do upload nunca toca o disco |
| Flask escutando só em `127.0.0.1` | Quem fala com a rede é o nginx |
| Remoção restrita a `img/novidades/` | Um id manipulado não apaga arquivo de outro lugar |
| Gravação do JSON em arquivo temporário | Queda de energia no meio não corrompe o conteúdo |
| Site público 100% estático | Nas páginas que o visitante acessa não há código para explorar |

O que **não** está feito e depende de vocês: HTTPS com certificado válido,
backup do `conteudo.json` e da pasta `img/novidades/`, e manter Python e
sistema atualizados.
