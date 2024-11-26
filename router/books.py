from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


@router.get('/', status_code=HTTPStatus.CREATED)
def create_book():
    return {'message': 'Book created!'}
