import cv2
import os
import sys
import torch
import pandas as pd

# Add the yolov5 directory to the system path
yolov5_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "yolov5"))
sys.path.append(yolov5_path)

# Import the required YOLOv5 components
from yolov5.models.experimental import attempt_load  # Correct import for loading the model
from src.config import YOLO_MODEL_PATH, IMAGE_DIR, DETECTION_DIR
from src.logger import setup_logger
from src.database import save_detection

logger = setup_logger()

class YOLODetector:
    def __init__(self):
        self.model = attempt_load(YOLO_MODEL_PATH)  # Load the model
        logger.info("Loaded YOLOv5 model.")

        # Get the class names from the model's metadata
        self.class_names = self.model.names if hasattr(self.model, 'names') else self.model.module.names
        logger.info(f"Class names: {self.class_names}")

    def detect_objects(self, image_path):
        """Detect objects in an image using YOLOv5."""
        logger.info(f"Processing image: {image_path}")

        # Verify the image file exists
        if not os.path.isfile(image_path):
            logger.error(f"Image file not found: {image_path}")
            return []

        # Verify the image file is readable
        try:
            with open(image_path, 'rb') as f:
                pass
        except Exception as e:
            logger.error(f"Unable to read image file {image_path}: {e}")
            return []

        # Load the image using OpenCV
        image = cv2.imread(image_path)
        if image is None:
            logger.error(f"Failed to load image: {image_path}")
            return []

        image = cv2.resize(image, (640, 640))  # Resize to model input size
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image_tensor = torch.from_numpy(image).float()
        image_tensor = image_tensor.permute(2, 0, 1).unsqueeze(0)  # Add batch dimension
        image_tensor /= 255.0  # Normalize

        # Perform inference
        results = self.model(image_tensor)

        # Access the detections
        detections = results[0] if isinstance(results, tuple) else results.xyxy[0]

        # Filter relevant detections
        detections = detections[detections[..., 4] > 0.5]  # Filter by confidence threshold, e.g., 0.5

        # Check if any detections exist
        if detections.shape[0] == 0:
            logger.info("No detections found.")
            return []

        # Convert to NumPy array and reshape for DataFrame
        detections = detections.cpu().numpy()[:, :6]  # Get the first 6 relevant columns
        logger.info(f"Detected {len(detections)} objects in {image_path}")

        # Save detection results manually
        os.makedirs(DETECTION_DIR, exist_ok=True)
        detection_file_path = os.path.join(DETECTION_DIR, os.path.basename(image_path).replace('.jpg', '_detections.csv'))
        
        # Create a DataFrame to save the detections
        df = pd.DataFrame(detections, columns=['x1', 'y1', 'x2', 'y2', 'confidence', 'class'])
        df.to_csv(detection_file_path, index=False)
        logger.info(f"Saved detection results to {detection_file_path}")

        return detections
    
    def process_detections(self, detections, image_path):
        """Process and save detections to the database."""
        for detection in detections:
            x1, y1, x2, y2, confidence, class_id = detection
            
            # Convert numpy types to Python native types
            x1, y1, x2, y2 = map(float, [x1, y1, x2, y2])  # Convert bounding box coordinates
            confidence = float(confidence)  # Convert confidence score
            class_name = self.class_names[int(class_id)]  # Assuming you have a mapping of class IDs to names

            # Save detection to the database
            save_detection(image_path, class_name, confidence, x1, y1, x2, y2)
            logger.info(f"Saved detection for {class_name} to the database.")