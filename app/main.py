from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base
from app.schemas import Detection, DetectionCreate
from app.crud import get_detection, get_detections, create_detection

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/detections/", response_model=Detection)
def create_detection_endpoint(detection: DetectionCreate, db: Session = Depends(get_db)):
    return create_detection(db, detection)

@app.get("/detections/", response_model=list[Detection])
def read_detections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    detections = get_detections(db, skip=skip, limit=limit)
    return detections

@app.get("/detections/{detection_id}", response_model=Detection)
def read_detection(detection_id: int, db: Session = Depends(get_db)):
    detection = get_detection(db, detection_id)
    if detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return detection