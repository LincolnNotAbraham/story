from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database  import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, index=True )
    password_hash = Column(String, index = True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    players = relationship("player",back_populates="user")

    