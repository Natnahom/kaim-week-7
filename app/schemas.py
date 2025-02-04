from pydantic import BaseModel

class DetectionBase(BaseModel):
    # Base schema for detection data
    image_path: str
    class_name: str
    confidence: float
    x1: int
    y1: int
    x2: int
    y2: int

class DetectionCreate(DetectionBase):
    # Schema for creating a new detection
    pass

class Detection(DetectionBase):
    # Schema for a detection with an ID
    id: int

    class Config:
        # Enable ORM mode to work with SQLAlchemy models
        orm_mode = True