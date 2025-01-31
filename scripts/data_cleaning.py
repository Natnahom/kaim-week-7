import pandas as pd
import numpy as np
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="data_cleaning.log"
)

def clean_data(input_file, output_file):
    """
    Clean the raw data and save it to a new CSV file.
    
    Args:
        input_file (str): Path to the raw data CSV file.
        output_file (str): Path to save the cleaned data.
    """
    try:
        logging.info(f"Loading raw data from {input_file}")
        df = pd.read_csv(input_file)

        # 1. Remove duplicates
        logging.info("Removing duplicates...")
        df.drop_duplicates(subset=["id"], inplace=True)

        # 2. Handle missing values
        logging.info("Handling missing values...")
        df["message"].fillna("", inplace=True)  # Fill missing messages with empty string
        df.dropna(subset=["date"], inplace=True)  # Drop rows with missing dates

        # 3. Standardize formats
        logging.info("Standardizing formats...")
        df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d %H:%M:%S")
        df["message"] = df["message"].str.strip().str.lower()

        # 4. Data validation
        logging.info("Validating data...")
        assert df["id"].is_unique, "Duplicate IDs found"
        assert df["date"].notna().all(), "Missing dates found"

        # Save cleaned data
        df.to_csv(output_file, index=False)
        logging.info(f"Cleaned data saved to {output_file}")

    except Exception as e:
        logging.error(f"Error during data cleaning: {e}")
