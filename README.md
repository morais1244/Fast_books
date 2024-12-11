# Projeto FastAPI

Este é um projeto FastAPI que fornece uma API RESTful para gerenciar livros. Cada usuário tem um banco de dados separado para seus livros.

## Funcionalidades

- Autenticação de usuários
- Conexão dinâmica com o banco de dados baseada no usuário autenticado
- Operações CRUD para livros

## Requisitos

- Python 3.12
- Poetry

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/seuusuario/fastapiproject.git
    cd fastapiproject
    ```

2. Instale as dependências usando o Poetry:

    ```sh
    poetry install
    ```

3. Configure o banco de dados:

    ```sh
    alembic upgrade head
    ```

## Executando a Aplicação

Para executar a aplicação localmente, use o seguinte comando:

```sh
poetry run uvicorn app:app --reload
```


## Docker

Para construir e executar a aplicação usando Docker, siga estes passos:  

1. Construa a imagem Docker:
   
 ```sh
  docker build -t fastapiproject .
 ```
  
3. Execute o container Docker:

```sh
  docker run -p 8000:8000 fastapiproject
```

A API estará disponível em http://127.0.0.1:8000.
