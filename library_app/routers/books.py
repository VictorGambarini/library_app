from pyexpat import model
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from library_app import models
from library_app.database import get_session
from sqlmodel import Session, select

router = APIRouter(prefix="/books", tags=["books"])

# Create a new book
@router.post("/create", response_model=models.Book)
def create_book(book: models.BookCreate, session: Session = Depends(get_session)):
    db_book = models.Book.from_orm(book)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

# Get a book by id
@router.get("/{book_id}", response_model=models.Book)
def read_book(book_id: int, session: Session = Depends(get_session)):
    db_book = session.get(models.Book, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return db_book

# Get list of all books
@router.get("/list/", response_model=List[models.BookRead])
def read_all_books(offset: int = 0, limit: int = Query(default=100, lte=100), session: Session = Depends(get_session)):
    books = session.exec(select(models.Book).offset(offset).limit(limit)).all()
    return books

# Update a book
@router.patch("/{book_id}", response_model=models.BookRead)
def update_book(book_id: int, book: models.BookUpdate, session: Session = Depends(get_session)):
    db_book = session.get(models.Book, book_id)
    if not book_id:
        raise HTTPException(status_code=404, detail="Book not found.")
    book_data = book.dict(exclude_unset=True)
    for k, v in book_data.items():
        setattr(db_book, k, v)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

# Delete a book
@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(models.Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    session.delete(book)
    session.commit()
    return {"Message": "Book deleted successfully."}