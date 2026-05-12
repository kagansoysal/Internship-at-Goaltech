from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Vote, Choice
from schemas.vote import VoteCreate, VoteResponse
from typing import List

router = APIRouter(prefix="/votes", tags=["Votes"])

@router.post("/", response_model=VoteResponse)
def create_vote(vote: VoteCreate, db: Session = Depends(get_db)):
    existing_vote = (
        db.query(Vote)
        .join(Choice, Vote.choice_id == Choice.id)
        .filter(Vote.user_id == vote.user_id, Choice.poll_id == vote.poll_id)
        .first()
    )

    if existing_vote:
        existing_vote.choice_id = vote.choice_id
        db.commit()
        db.refresh(existing_vote)
        return existing_vote

    new_vote = Vote(user_id=vote.user_id, choice_id=vote.choice_id)
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return new_vote


@router.get("/poll/{poll_id}", response_model=List[VoteResponse])
def get_votes_for_poll(poll_id: int, db: Session = Depends(get_db)):
    votes = db.query(Vote).join(Choice).filter(Choice.poll_id == poll_id).all()
    return votes