from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database  import Base

class Player(Base):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    id_user=Column(Integer, ForeignKey("users.id"), nullablr=True)
    session_id = Column(String, index=True)
    name = Column(String)

    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)

    attributes = Column(JSON, default={"strength": 10, "intelligence": 10, "agility": 10})
    itens = Column (JSON, default={""})

    current_health = Column(Integer, default=100)
    max_health = Column(Integer, default=100)

    stories_complette = Column(Integer,  default=0)
    stories = relationship("stories", back_populates="player_id")
    user = relationship("users", back_populates="players")