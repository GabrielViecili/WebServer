# API Flask Simples com Autenticação

Este é um projeto de API construído com Flask que demonstra as melhores práticas de desenvolvimento, incluindo a separação de responsabilidades e autenticação baseada em token.

A API permite adicionar e consultar dados em um banco de dados SQLite, com as rotas protegidas por uma chave de API.

## Estrutura do Projeto

* `app.py`: O ponto de entrada da aplicação. Define as rotas da API (`/api/data`), lida com as requisições HTTP e orquestra a lógica de negócio.
* `database.py`: Módulo de acesso a dados. Contém todas as funções que interagem com o banco de dados SQLite.
* `auth.py`: Módulo de autenticação. Fornece o decorator `@token_required` para proteger as rotas.
* `data.db`: O arquivo do banco de dados SQLite (criado na primeira execução).
* `requirements.txt`: Arquivo que lista as dependências do projeto.

## Como Executar

### Pré-requisitos

* Python 3.x
* `pip`

### Passos

1.  **Clone o Repositório**
    ```bash
    # Substitua pela URL do seu repositório
    git clone [https://github.com/GabrielViecili/WebServer.git]
    cd seu-repositorio
    ```

2.  **Crie um Ambiente Virtual (Recomendado)**
    ```bash
    python -m venv venv
    ```
    * No Windows: `venv\Scripts\activate`
    * No macOS/Linux: `source venv/bin/activate`

3.  **Instale as Dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a Aplicação**
    ```bash
    python app.py
    ```
    O servidor será iniciado em `http://127.0.0.1:5000`. Na primeira vez que for executado, o arquivo `data.db` será criado.

## Como Usar a API

Todas as requisições para a API precisam de um cabeçalho de autorização. O token padrão definido no arquivo `auth.py` é `SENHA_SUPER_SECRETA_123`.

### 1. Adicionar um Dado (POST `/api/data`)

Envia um novo valor para ser armazenado no banco de dados.

**Exemplo com `curl`:**
```bash
curl -X POST [http://127.0.0.1:5000/api/data](http://127.0.0.1:5000/api/data) \
-H "Content-Type: application/json" \
-H "Authorization: Bearer SENHA_SUPER_SECRETA_123" \
-d '{"data": "Este é um novo valor"}'
```

Resposta de Sucesso (Código 201):

```JSON

{
  "message": "Valor adicionado com sucesso"
};
```

### 2. Obter Todos os Dados (GET /api/data)

Retorna uma lista de todos os dados armazenados.

**Exemplo com curl:**
```Bash

curl [http://127.0.0.1:5000/api/data](http://127.0.0.1:5000/api/data) \
-H "Authorization: Bearer SENHA_SUPER_SECRETA_123"
```

**Resposta de Sucesso (Código 200):**

```JSON

[
  {
    "created_at": "2023-10-27 15:30:00",
    "id": 1,
    "value": "Este é um novo valor"
  }
]
```

### Respostas de Erro Comuns

* **400 Bad Request:** Se o corpo da requisição não for JSON ou se o campo `data` estiver faltando.
* **401 Unauthorized:** Se o token de autorização estiver faltando ou for inválido.
* **404 Not Found:** Se a rota acessada não existir.
* **500 Internal Server Error:** Se ocorrer um erro inesperado no servidor.