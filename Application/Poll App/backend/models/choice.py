from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    poll_id = Column(Integer, ForeignKey("polls.id"))
    choice_text = Column(String, nullable=False)
    votes = relationship("Vote", back_populates="choice", cascade="all, delete-orphan")
    poll = relationship("Poll", back_populates="choices")