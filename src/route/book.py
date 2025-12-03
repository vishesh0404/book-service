from fastapi import FastAPI
from typing import Annotated
from sqlmodel import Session

from src.db.db import get_session

from src.model.books import Books
from src.service.book import get_all_books, get_book_by_id, delete_book, add_book

app = FastAPI()

version = "v1"

# List all books
@app.get("/v1/books/")
def get_all_books(db : Annotated[Session, get_session()]) -> list[Books]:
    return get_all_books(db)

@app.get("/v1/books/{id}")
def get_book(id : int , db : Annotated[Session, get_session()]):
    return get_book_by_id(id , db)

@app.put("/v1/books/{id}")
def update_book(id : int, db : Annotated[Session, get_session()]):
    return "Book Object" ## ToDo - get from DB

@app.delete("/v1/books/{id}")
def delete_book(id: int, db : Annotated[Session, get_session()]):
    return delete_book(id , db)
@app.post("/v1/books/")
def add_book(book: Books , db : Annotated[Session, get_session()]):
    return add_book(book , db)