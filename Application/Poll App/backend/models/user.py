from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Enum 
from sqlalchemy.orm import relationship
from enums import UserRole

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    
    votes = relationship("Vote", back_populates="user")