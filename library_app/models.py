from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship


class MemberBase(SQLModel):
    name: str = Field(index=True)
    email: str = Field(index=True)
    is_active: Optional[bool] = Field(default=True)
    n_books_rented: Optional[int] = Field(default=0, index=True)
    debt: Optional[float] = Field(default=0, index=True)


class Member(MemberBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    books: List["Book"] = Relationship(back_populates="member")
    

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
    member_id: Optional[int] = Field(default=None, foreign_key="member.id")


class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    member: Optional[Member] = Relationship(back_populates="books")


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int


class BookUpdate(SQLModel):
    title: Optional[str] = None
    authors: Optional[str] = None
    isbn: Optional[str] = None
    isbn13: Optional[str] = None
    language_code: Optional[str] = None
    num_pages: Optional[int] = 0
    ratings_count: Optional[int] = 0
    text_reviews_count: Optional[int] = 0
    publication_date:Optional[str] = None
    publisher: Optional[str] = None
    average_rating: Optional[float] = 0
    description: Optional[str] = None
    member_id: Optional[int] = Field(default=None, foreign_key="member.id")