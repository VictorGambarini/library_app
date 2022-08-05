from typing import List, Union
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: Union[str, None] = None
    title: str
    authors: str
    isbn: str
    isbn13: str
    language_code: str
    num_pages: int
    ratings_count: int
    text_reviews_count: int
    publication_date: str
    publisher: str
    average_rating: float
    description: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    book: List[Book] = []

    class Config:
        orm_mode = True