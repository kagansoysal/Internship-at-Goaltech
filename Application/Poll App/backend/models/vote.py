from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Vote(Base):
    __tablename__ = "votes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    choice_id = Column(Integer, ForeignKey("choices.id"))
    
    user = relationship("User", back_populates="votes")
    choice = relationship("Choice", back_populates="votes")
