from dataclasses import asdict

from sqlalchemy import select

from database.models import Book


def test_create_user(session):
    new_book = Book(
        title='Harry Potter',
        author='J.K. Rowling',
        description='A book about magic',
    )
    session.add(new_book)
    session.commit()

    book = session.scalar(select(Book).where(Book.title == 'Harry Potter'))

    assert asdict(book) == {
        'id': 1,
        'title': 'Harry Potter',
        'author': 'J.K. Rowling',
        'description': 'A book about magic',
        'created_at': book.created_at,
    }
