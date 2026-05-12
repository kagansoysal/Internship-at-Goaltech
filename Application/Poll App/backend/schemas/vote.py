from pydantic import BaseModel

class VoteBase(BaseModel):
    choice_id: int
    user_id: int

class VoteCreate(VoteBase):
    poll_id: int
    pass

class VoteResponse(VoteBase):
    id: int

    class Config:
        orm_mode = True
