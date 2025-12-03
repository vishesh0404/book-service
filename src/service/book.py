from sqlmodel import Session, select
from src.model.books import Books

def get_all_books(session : Session):
    books = Session.exec(select(Books)).all()
    return books

def get_book_by_id(id: int ,session : Session):
    books = session.get(Books, id)
    return books


def add_book(book: Books ,session : Session):
    books = session.add(book)
    return books

def delete_book(book: Books ,session : Session):
    books = session.delete(book)