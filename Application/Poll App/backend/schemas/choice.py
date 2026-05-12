from pydantic import BaseModel
from typing import List, Optional
from schemas.vote import VoteResponse

class ChoiceBase(BaseModel):
    choice_text: str

class ChoiceCreate(ChoiceBase):
    poll_id: int

class ChoiceUpdate(BaseModel):
    choice_text: Optional[str] = None

class ChoiceResponse(ChoiceBase):
    id: int
    votes: List["VoteResponse"] = []

    class Config:
        orm_mode = True

ChoiceResponse.model_rebuild()