from sqlmodel import Field, SQLModel

class Books(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str | None = Field(nullable=False)
    author: str
    year: int
    isbn: str
    available: bool | None = Field(default=True)
