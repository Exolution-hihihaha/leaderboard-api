from sqlalchemy import Column, Integer, String, DateTime, func
from app.db import Base

class Score(Base):
    __tablename__ = "leaderboard"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
