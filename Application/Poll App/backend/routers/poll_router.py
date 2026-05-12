from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Poll
from schemas.poll import PollCreate, PollUpdate, PollResponse
from typing import List

router = APIRouter(prefix="/polls", tags=["Polls"])

@router.post("/", response_model=PollResponse)
def create_poll(poll: PollCreate, db: Session = Depends(get_db)):
    new_poll = Poll(**poll.dict())
    db.add(new_poll)
    db.commit()
    db.refresh(new_poll)
    return new_poll

@router.get("/", response_model=List[PollResponse])
def get_polls(db: Session = Depends(get_db)):
    return db.query(Poll).all()

@router.get("/{poll_id}", response_model=PollResponse)
def get_poll(poll_id: int, db: Session = Depends(get_db)):
    poll = db.query(Poll).filter(Poll.id == poll_id).first()
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    return poll

@router.put("/{poll_id}", response_model=PollResponse)
def update_poll(poll_id: int, updated_poll: PollUpdate, db: Session = Depends(get_db)):
    poll = db.query(Poll).filter(Poll.id == poll_id).first()
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    for key, value in updated_poll.dict(exclude_unset=True).items():
        setattr(poll, key, value)
    db.commit()
    db.refresh(poll)
    return poll

@router.delete("/{poll_id}")
def delete_poll(poll_id: int, db: Session = Depends(get_db)):
    poll = db.query(Poll).filter(Poll.id == poll_id).first()
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    db.delete(poll)
    db.commit()
    return {"message": "Poll deleted successfully"}
