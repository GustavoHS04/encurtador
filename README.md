# Encurtador de links

API REST para gerar códigos curtos para URLs, redirecionar quem acessa esses
códigos e consultar estatísticas de acesso. A aplicação usa FastAPI e SQLite.

## Requisitos

- Python 3.10 ou superior
- `pip`

O `requirements.txt` atual não lista as dependências usadas pela aplicação.
Instale-as diretamente no ambiente virtual, como mostrado abaixo.

## Instalação e execução

Na raiz do projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn pytest
mkdir -p data
uvicorn app.main:app --reload
```

O servidor fica disponível em <http://127.0.0.1:8000>. A documentação
interativa da API pode ser acessada em <http://127.0.0.1:8000/docs>.

O banco SQLite é criado em `data/links.db`; as tabelas são inicializadas ao
iniciar a aplicação. O diretório `data/` precisa existir antes da primeira
execução.

## Endpoints

### Criar um link curto

`POST /encurtar` recebe uma URL no corpo JSON. O parâmetro opcional `tam`
define o tamanho do código, de 4 a 12 caracteres (padrão: 6).

```bash
curl -X POST 'http://127.0.0.1:8000/encurtar?tam=6' \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com/artigo"}'
```

Exemplo de resposta:

```json
{
  "codigo": "a1B2c3",
  "link_curto": "http://127.0.0.1:8000/a1B2c3"
}
```

Não são aceitos links cujo host seja `localhost` ou um endereço IP de loopback
ou não especificado, para evitar apontar o redirecionamento para o próprio
ambiente local.

### Acessar o link curto

Abra `GET /{codigo}` para registrar um acesso e receber um redirecionamento
para a URL original. Por exemplo:

```bash
curl -i 'http://127.0.0.1:8000/a1B2c3'
```

### Consultar estatísticas de um link

`GET /estatisticas/{codigo}` retorna o código, a URL original e a quantidade
de acessos registrados:

```bash
curl 'http://127.0.0.1:8000/estatisticas/a1B2c3'
```

### Listar links mais acessados

`GET /top` retorna o ranking ordenado pela quantidade de acessos. O parâmetro
opcional `limite` aceita valores de 1 a 50 (padrão: 5):

```bash
curl 'http://127.0.0.1:8000/top?limite=10'
```

## Testes

Com o ambiente virtual ativado, execute:

```bash
python -m pytest
```
