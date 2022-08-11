from sqlmodel import create_engine, SQLModel, Session
from library_app import models
from library_app.config import secrets

connect_args = {"check_same_thread": False}
engine = create_engine(secrets.SQLITE_DATABASE_URL, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def main():
    create_db_and_tables()

if __name__ == "__main__":
    main()        