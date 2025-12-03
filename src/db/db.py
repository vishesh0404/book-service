from sqlmodel import Session, SQLModel, create_engine

connect_args = {"check_same_thread": False}
engine = create_engine("sqlite:///book_service.db" , connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session