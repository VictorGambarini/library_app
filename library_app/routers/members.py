from typing import List
from fastapi import APIRouter, HTTPException, Query, Depends
from library_app import models
from library_app.database import get_session
from sqlmodel import Session, select

router = APIRouter(prefix="/members", tags=["members"])

# Create a new member
@router.post("/create", response_model=models.MemberRead)
def create_member(member: models.MemberCreate, session: Session = Depends(get_session)):
    db_member = models.Member.from_orm(member)      
    session.add(db_member)
    session.commit()
    session.refresh(db_member)
    return db_member

# Get a member by id
@router.get("/{member_id}", response_model=models.MemberRead)
def read_member(member_id: int, session: Session = Depends(get_session)):
    member = session.get(models.Member, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found.")
    return member

# Get a list with all members
@router.get("/list/", response_model=List[models.MemberRead])
def read_all_members(offset: int = 0, limit: int = Query(default=100, lte=100), session: Session = Depends(get_session)):
    members = session.exec(select(models.Member).offset(offset).limit(limit)).all()
    return members

# Update a member
@router.patch("/{member_id}", response_model=models.MemberRead)
def update_member(member_id: int, member: models.MemberUpdate, session: Session = Depends(get_session)):
    db_member = session.get(models.Member, member_id)
    if not db_member:
        raise HTTPException(status_code=404, detail="Member not found.")
    member_data = member.dict(exclude_unset=True)
    for k, v in member_data.items():
        setattr(db_member, k, v)
    session.add(db_member)
    session.commit()
    session.refresh(db_member)
    return db_member

# Delete member
@router.delete("/{member_id}")
def delete_member(member_id: int, session: Session = Depends(get_session)):
    member = session.get(models.Member, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found.")
    session.delete(member)
    session.commit()
    return {"Message": "Member deleted successfully."}