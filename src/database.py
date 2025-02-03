import psycopg2
from psycopg2 import sql
from src.config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def get_db_connection():
    """Create and return a PostgreSQL database connection."""
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def create_detections_table():
    """Create the detections table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS detections (
        id SERIAL PRIMARY KEY,
        image_path TEXT,
        class_name TEXT,
        confidence FLOAT,
        x1 INT,
        y1 INT,
        x2 INT,
        y2 INT
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

def save_detection(image_path, class_name, confidence, x1, y1, x2, y2):
    """Save detection results to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO detections (image_path, class_name, confidence, x1, y1, x2, y2)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, (image_path, class_name, confidence, x1, y1, x2, y2))
    conn.commit()
    cursor.close()
    conn.close()