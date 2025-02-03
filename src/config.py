import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# YOLO model configuration
YOLO_MODEL_PATH = "../yolov5/models/yolov5s.pt"  # Path to the YOLOv5 model
IMAGE_DIR = "../../data/images"  # Directory containing images
DETECTION_DIR = "data/detections"  # Directory to save detection results

# Database configuration
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")