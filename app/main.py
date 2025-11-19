from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db import Base, engine, SessionLocal
from app import crud, schemas, models

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/submit_score")
def submit_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    return crud.create_score(db, score)

@app.get("/leaderboard")
def leaderboard(db: Session = Depends(get_db)):
    return crud.get_leaderboard(db)

@app.get("/")
def root():
    return {"status": "OK", "message": "Leaderboard API is running"}