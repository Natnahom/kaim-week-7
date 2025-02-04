import logging

def setup_logger(log_file="object_detection.log"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=log_file
    )
    return logging.getLogger()