from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Detection(Base):
    # SQLAlchemy model for the detections table
    __tablename__ = "detections"
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the detection
    image_path = Column(String)  # Path to the image
    class_name = Column(String)  # Name of the detected class
    confidence = Column(Float)    # Confidence score of the detection
    x1 = Column(Integer)          # X coordinate of top-left corner
    y1 = Column(Integer)          # Y coordinate of top-left corner
    x2 = Column(Integer)          # X coordinate of bottom-right corner
    y2 = Column(Integer)          # Y coordinate of bottom-right corner