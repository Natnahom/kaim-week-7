from sqlalchemy.orm import Session
from app.models import Detection
from app.schemas import DetectionCreate

def get_detection(db: Session, detection_id: int):
    # Retrieve a single detection by its ID
    return db.query(Detection).filter(Detection.id == detection_id).first()

def get_detections(db: Session, skip: int = 0, limit: int = 100):
    # Retrieve a list of detections with pagination
    return db.query(Detection).offset(skip).limit(limit).all()

def create_detection(db: Session, detection: DetectionCreate):
    # Create a new detection entry in the database
    db_detection = Detection(**detection.dict())
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection