from http import HTTPStatus

from fastapi import FastAPI
from sqlalchemy import create_engine

from database.models import table_registry
from router import auth, books, users
from settings import Settings

app = FastAPI()

# Create the database tables
engine = create_engine(Settings().DATABASE_URL)
table_registry.metadata.create_all(engine)

app.include_router(books.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá Mundo!'}
