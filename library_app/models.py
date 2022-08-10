from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine


class MemberBase(SQLModel):
    name: str = Field(index=True)
    email: str = Field(index=True)
    is_active: Optional[bool] = Field(default=True)
    n_books_rented: Optional[int] = Field(default=0, index=True)
    debt: Optional[float] = Field(default=0, index=True)


class Member(MemberBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    

class MemberCreate(SQLModel):
    name: str
    email: str


class MemberRead(MemberBase):
    id: int


class MemberUpdate(MemberBase):
    name: Optional[str] = None
    email: Optional[str] = None


class BookBase(SQLModel):
    title: str = Field(index=True)
    authors: str = Field(index=True)
    isbn: str = Field(index=True)
    isbn13: str = Field(index=True)
    language_code: str = Field(index=True)
    num_pages: int = Field(index=True)
    ratings_count: int = Field(index=True)
    text_reviews_count: int = Field(index=True)
    publication_date: str = Field(index=True)
    publisher: str = Field(index=True)
    average_rating: float = Field(index=True)
    description: str



class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int