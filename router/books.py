from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database.database import get_session
from database.models import Book
from schemas import BookSchema

router = APIRouter()


@router.post(
    '/books/', status_code=HTTPStatus.CREATED, response_model=BookSchema
)
def create_book(book: BookSchema, session: Session = Depends(get_session)):
    db_book = session.scalar(select(Book).where(Book.title == book.title))
    if db_book:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Book already exists'
        )
    db_book = Book(
        title=book.title, author=book.author, description=book.description
    )
    session.add(db_book)
    session.commit()
    session.refresh(db_book)

    return db_book


@router.get(
    '/books/', status_code=HTTPStatus.OK, response_model=list[BookSchema]
)
def read_books(session: Session = Depends(get_session)):
    books = session.scalars(select(Book)).all()
    return books


@router.put(
    '/books/{book_id}/', status_code=HTTPStatus.OK, response_model=BookSchema
)
def update_book(
    book_id: int, book: BookSchema, session: Session = Depends(get_session)
):
    db_book = session.scalar(select(Book).where(Book.id == book_id))
    if not db_book:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Book not found'
        )
    try:
        db_book.title = book.title
        db_book.author = book.author
        db_book.description = book.description
        session.commit()
        session.refresh(db_book)
        return db_book
    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Book already exists'
        )


@router.delete('/books/{book_id}/')
def delete_book(book_id: int, session: Session = Depends(get_session)):
    db_book = session.scalar(select(Book).where(Book.id == book_id))
    if not db_book:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Book not found'
        )
    session.delete(db_book)
    session.commit()
    return {'message': 'Book deleted'}
