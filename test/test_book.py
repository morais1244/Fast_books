from http import HTTPStatus

from schemas import BookSchema


def test_create_book(client):
    response = client.post(
        '/books/',
        json={
            'title': 'Harry Potter',
            'author': 'J.K. Rowling',
            'description': 'A book about magic',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'title': 'Harry Potter',
        'author': 'J.K. Rowling',
        'description': 'A book about magic',
    }


def test_read_users_empty(client):
    response = client.get('/books/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == []


def test_read_books(client, book):
    book_schema = BookSchema.model_validate(book).model_dump()
    response = client.get('/books/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [book_schema]


def test_update_book(client, book):
    response = client.put(
        f'/books/{book.id}/',
        json={
            'title': 'Harry Potter and the Chamber of Secrets',
            'author': 'J.K. Rowling',
            'description': 'A book about magic',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'title': 'Harry Potter and the Chamber of Secrets',
        'author': 'J.K. Rowling',
        'description': 'A book about magic',
    }


def test_update_book_not_found(client):
    response = client.put(
        '/books/1/',
        json={
            'title': 'Harry Potter and the Chamber of Secrets',
            'author': 'J.K. Rowling',
            'description': 'A book about magic',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Book not found'}


def test_delete_user(client, book):
    response = client.delete('/books/1/')
    assert response.json() == {'message': 'Book deleted'}
