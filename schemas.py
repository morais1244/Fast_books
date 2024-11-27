from pydantic import BaseModel, ConfigDict
from pygments.lexer import default


class BookSchema(BaseModel):
    title: str
    author: str
    description: str = default('No description')
    model_config = ConfigDict(from_attributes=True)


from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
