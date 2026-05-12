from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Choice
from schemas.choice import ChoiceCreate, ChoiceResponse
from typing import List

router = APIRouter(prefix="/choices", tags=["Choices"])

@router.post("/", response_model=ChoiceResponse)
def create_choice(choice: ChoiceCreate, db: Session = Depends(get_db)):
    new_choice = Choice(**choice.dict())
    db.add(new_choice)
    db.commit()
    db.refresh(new_choice)
    return new_choice

@router.get("/poll/{poll_id}", response_model=List[ChoiceResponse])
def get_choices_by_poll(poll_id: int, db: Session = Depends(get_db)):
    choices = db.query(Choice).filter(Choice.poll_id == poll_id).all()
    if not choices:
        raise HTTPException(status_code=404, detail="Choices not found for this poll")
    return choices

@router.delete("/{choice_id}")
def delete_choice(choice_id: int, db: Session = Depends(get_db)):
    choice = db.query(Choice).filter(Choice.id == choice_id).first()
    if not choice:
        raise HTTPException(status_code=404, detail="Choice not found")
    db.delete(choice)
    db.commit()
    return {"message": "Choice deleted successfully"}
