from curses.ascii import isblank
from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from library_app.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    book = relationship("Book", back_populates="owner")


class Book(Base):
    __tablename__ = "book"    

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    authors = Column(String, index=True)
    isbn = Column(String, index=True)
    isbn13 = Column(String, index=True)
    language_code = Column(String, index=True)
    num_pages = Column(Integer, index=True)
    ratings_count = Column(Integer, index=True)
    text_reviews_count = Column(Integer, index=True)
    publication_date = Column(String, index=True)
    publisher = Column(String, index=True)
    average_rating = Column(Float, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="book")