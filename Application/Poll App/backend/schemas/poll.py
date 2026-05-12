from pydantic import BaseModel
from typing import List, Optional, TYPE_CHECKING
from schemas.choice import ChoiceResponse


class PollBase(BaseModel):
    question: str

class PollCreate(PollBase):
    pass

class PollUpdate(BaseModel):
    question: Optional[str] = None

class PollResponse(PollBase):
    id: int
    is_active: bool = True
    choices: List["ChoiceResponse"] = []

    class Config:
        orm_mode = True

PollResponse.model_rebuild()