from sqlalchemy.orm import Session
from app import models, schemas

def create_score(db: Session, score: schemas.ScoreCreate):
    db_score = models.Score(name=score.name, score=score.score)
    db.add(db_score)
    db.commit()
    return db_score

def get_leaderboard(db: Session, limit: int = 20):
    return db.query(models.Score).order_by(models.Score.score.desc()).limit(limit).all()
