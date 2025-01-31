import psycopg2
from psycopg2 import sql
import pandas as pd
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables for api credentials
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

def save_to_postgresql(data_file, table_name):
    """
    Save cleaned data to a PostgreSQL database.
    
    Args:
        data_file (str): Path to the cleaned data CSV file.
        table_name (str): Name of the table to create or append to.
    """
    try:
        # Database connection parameters
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Load cleaned data
        df = pd.read_csv(data_file)

        # Ensure 'views' column exists
        if 'views' in df.columns:
            # Convert views column to numeric, coercing errors to NaN
            df['views'] = pd.to_numeric(df['views'], errors='coerce')
            
            # Replace NaN or empty strings with 0 or None for empty cells
            df['views'] = df['views'].fillna(0)  # Use 0 for empty cells
            # If you want to use None instead, uncomment the line below:
            # df['views'] = df['views'].where(pd.notna(df['views']), None)
        else:
            logging.warning(f"'views' column not found in {data_file}.")
            
        # Create table if it doesn't exist
        create_table_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS {} (
                id BIGINT PRIMARY KEY,
                date TIMESTAMP,
                message TEXT,
                views INT,
                media BOOLEAN
            );
        """).format(sql.Identifier(table_name))
        cursor.execute(create_table_query)

        # Insert data
        for _, row in df.iterrows():
            insert_query = sql.SQL("""
                INSERT INTO {} (id, date, message, views, media)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """).format(sql.Identifier(table_name))
            cursor.execute(insert_query, tuple(row))

        # Commit and close
        conn.commit()
        cursor.close()
        conn.close()
        logging.info(f"Data saved to PostgreSQL table {table_name}")

    except Exception as e:
        logging.error(f"Error saving data to PostgreSQL: {e}")
