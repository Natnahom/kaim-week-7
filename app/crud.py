from sqlalchemy.orm import Session
from app.models import Detection
from app.schemas import DetectionCreate

def get_detection(db: Session, detection_id: int):
    return db.query(Detection).filter(Detection.id == detection_id).first()

def get_detections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Detection).offset(skip).limit(limit).all()

def create_detection(db: Session, detection: DetectionCreate):
    db_detection = Detection(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection