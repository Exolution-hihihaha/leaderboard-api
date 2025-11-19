from pydantic import BaseModel
from datetime import datetime

class ScoreCreate(BaseModel):
    name: str
    score: int

class ScoreItem(BaseModel):
    name: str
    score: int
    timestamp: datetime

    class Config:
        orm_mode = True
