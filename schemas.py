from pydantic import BaseModel, ConfigDict
from pygments.lexer import default


class BookSchema(BaseModel):
    title: str
    author: str
    description: str = default('No description')
    model_config = ConfigDict(from_attributes=True)


# Compare this snippet from database/db.py:
