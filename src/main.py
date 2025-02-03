from config import IMAGE_DIR
import sys
import os

# Add the yolov5 directory to the Python path
yolov5_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "yolov5"))
sys.path.append(yolov5_path)

from detector import YOLODetector
from database import create_detections_table
from logger import setup_logger

logger = setup_logger()

def main():
    # Create the detections table in the database
    create_detections_table()
    logger.info("Created detections table in the database.")

    # Initialize the YOLO detector
    detector = YOLODetector()

    # Process all images in the IMAGE_DIR
    for image_name in os.listdir(IMAGE_DIR):
        image_path = os.path.join(IMAGE_DIR, image_name)
        if os.path.isfile(image_path):
            detections = detector.detect_objects(image_path)
            detector.process_detections(detections, image_path)

if __name__ == "__main__":
    main()