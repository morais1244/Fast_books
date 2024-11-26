from http import HTTPStatus

from fastapi import FastAPI

from router import books

app = FastAPI()

app.include_router(books.router)


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá Mundo!'}
