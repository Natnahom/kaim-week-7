import cv2
import os
import sys
import torch

# Add the yolov5 directory to the system path
yolov5_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "yolov5"))
sys.path.append(yolov5_path)

# Import the required YOLOv5 components
from yolov5.models.experimental import attempt_load  # Correct import for loading the model
from src.config import YOLO_MODEL_PATH, IMAGE_DIR, DETECTION_DIR
from src.logger import setup_logger

logger = setup_logger()

class YOLODetector:
    def __init__(self):
        self.model = attempt_load(YOLO_MODEL_PATH)  # Load the model
        logger.info("Loaded YOLOv5 model.")

    def detect_objects(self, image_path):
        """Detect objects in an image using YOLOv5."""
        logger.info(f"Processing image: {image_path}")
        
        # Load the image using OpenCV
        image = cv2.imread(image_path)
        
        # Convert the image from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Convert the image to a tensor and add a batch dimension
        image_tensor = torch.from_numpy(image).float()  # Convert to float tensor
        image_tensor = image_tensor.permute(2, 0, 1)  # Change dimensions from HWC to CHW
        image_tensor = image_tensor.unsqueeze(0)  # Add batch dimension

        # Normalize the image (if required by your model)
        image_tensor /= 255.0  # Scale pixel values to [0, 1]

        # Perform inference
        results = self.model(image_tensor)  # Perform inference
        detections = results.xyxy[0].cpu().numpy()  # Get detections as a NumPy array
        logger.info(f"Detected {len(detections)} objects in {image_path}")

        # Save detection results
        os.makedirs(DETECTION_DIR, exist_ok=True)
        results.save(DETECTION_DIR)
        logger.info(f"Saved detection results to {DETECTION_DIR}")

        return detections

    def process_detections(self, detections, image_path):
        """Process detection results and save to the database."""
        for detection in detections:
            x1, y1, x2, y2, confidence, class_id = detection
            class_name = self.model.names[int(class_id)]  # Get class name
            logger.info(f"Detected {class_name} with confidence {confidence:.2f} at [{x1}, {y1}, {x2}, {y2}]")

            # Save detection to the database
            from database import save_detection
            save_detection(image_path, class_name, confidence, x1, y1, x2, y2)
            logger.info(f"Saved detection for {class_name} to the database.")