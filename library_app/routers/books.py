from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from library_app import models, schemas
from library_app.database import SessionLocal, engine, get_db

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/{user_id}", response_model=schemas.Book)
def create_book_for_user(
    user_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)
):
    db_book = models.Book(**book.dict(), owner_id=user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/", response_model=List[schemas.Book])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Book).offset(skip).limit(limit).all()