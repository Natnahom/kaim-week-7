from pydantic import BaseModel

class DetectionBase(BaseModel):
    image_path: str
    class_name: str
    confidence: float
    x1: int
    y1: int
    x2: int
    y2: int

class DetectionCreate(DetectionBase):
    pass

class Detection(DetectionBase):
    id: int

    class Config:
        orm_mode = True