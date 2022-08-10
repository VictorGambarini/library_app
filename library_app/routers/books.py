from fastapi import APIRouter, Depends, HTTPException
from typing import List
from library_app import models
from library_app.database import engine, get_session

router = APIRouter(prefix="/books", tags=["books"])

# @router.post("/{book_id}", response_model=models.Book)
# def create_book_for_member(
#     user_id: int, book: models.Book, db: get_session()):

#     db_book = models.Book(**book.dict(), owner_id=user_id)
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
#     return db_book

# @router.get("/", response_model=List[models.Book])
# def read_items(*, skip: int = 0, limit: int = 100, db: get_session()):
#     return db.query(models.Book).offset(skip).limit(limit).all()