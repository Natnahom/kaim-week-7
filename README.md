## This is Week-7 of 10 academy

# Task 1: Data Scraping and Collection Pipeline
This project involves building a data scraping and collection pipeline to extract data from Telegram channels related to Ethiopian medical businesses. The scraped data is stored in CSV files for further processing and analysis.

## Overview
The goal of this task is to:

- Scrape data from public Telegram channels using the telethon library.

- Store the scraped data (messages, metadata, etc.) in CSV files.

- Prepare the data for further processing in the data pipeline.

## Features
1. Telegram Scraping: Extracts messages, metadata (e.g., date, views), and media information from Telegram channels.

2. Modular Code: The script is designed to be reusable and scalable.

3. Logging: Detailed logs are generated to track the scraping process and debug issues.

4. Graceful Shutdown: Handles interruptions (e.g., Ctrl+C) gracefully to ensure resources are properly cleaned up.

## Prerequisites
Before running the script, ensure you have the following:

- Python 3.9 or higher: Install Python from python.org.

# Telegram API Credentials:

- Obtain API_ID and API_HASH from my.telegram.org.

- Use your phone number in international format (e.g., +251912345678).

# Required Python Libraries:
- Install the required libraries using the following command:

- pip install telethon pandas python-dotenv
## Setup
Clone the Repository:

# Set Up Environment Variables:
Create a .env file in the root directory and add your Telegram API credentials:

- API_ID=your_api_id
- API_HASH=your_api_hash
- PHONE_NUMBER=+251912345678
# Update the Script:
- Modify the CHANNELS list in the script to include the Telegram channels you want to scrape:

- CHANNELS = ["DoctorsET", "Chemed", "lobelia4cosmetics", "yetenaweg", "EAHCI"]
## Running the Script
Navigate to the project directory:

cd scripts
Run the script:

python telegram_scraper.py
# Monitor Progress:

- The script logs progress to the console and a log file (telegram_scraping.log).

- Scraped data is saved in the raw_data directory as CSV files.

## Output
The scraped data is stored in the raw_data directory. Each channel has its own CSV file with the following columns:

- id: Unique message ID.

- date: Timestamp of the message.

- message: Text content of the message.

- views: Number of views (if available).

- media: Boolean indicating whether the message contains media.

- Example file: raw_data/DoctorsET_messages.csv

# Logs
- Detailed logs are saved in telegram_scraping.log. The log file includes:

Connection status.

Progress of the scraping process.

Errors and warnings (if any).

Troubleshooting
Connection Issues:

Ensure your internet connection is stable.

Verify that your API credentials are correct.

Rate Limits:

If you encounter rate limits, increase the delay between requests by modifying the await asyncio.sleep(2) line in the script.

# Logs:

Check the telegram_scraping.log file for detailed error messages.

## Next Steps
Extend Functionality:

Add image scraping for object detection using YOLO.

Implement data cleaning and transformation pipelines.

Integrate with Data Warehouse:

Load the scraped data into a data warehouse (e.g., PostgreSQL) for further analysis.

# Task 2: Data Cleaning and Transformation Pipeline
- This project involves cleaning and transforming scraped data from Telegram channels related to Ethiopian medical businesses. The cleaned data is stored in a PostgreSQL database and transformed using DBT (Data Build Tool) for advanced analysis.

## Overview
The goal of this task is to:

1. Clean the raw data by handling missing values, duplicates, and inconsistencies.

2. Transform the data into a structured format suitable for analysis.

3. Store the cleaned data in a PostgreSQL database.

4. Use DBT for advanced data transformation and testing.

## Features
- Data Cleaning:

    - Removes duplicates, handles missing values, and standardizes formats.

    - Validates data to ensure consistency.

- Data Storage:

    - Stores cleaned data in PostgreSQL tables.

- DBT for Transformation:

    - Defines SQL models for advanced transformations.

    - Runs tests to ensure data quality.

    - Generates documentation for the project.

- Logging:

    - Detailed logs track the cleaning and transformation process.

## Prerequisites
Before running the pipeline, ensure you have the following:

- Python 3.9 or higher: Install Python from python.org.

- PostgreSQL: Install PostgreSQL from postgresql.org.

- Required Python Libraries:
Install the required libraries using the following command:

    - pip install pandas psycopg2 python-dotenv
- DBT: Install DBT using:

    - pip install dbt-core dbt-postgres

## Setup
- Clone the Repository
- Set Up Environment Variables
Create a .env file in the root directory and add your PostgreSQL credentials:

    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_host
    DB_PORT=your_port_number

3. Create PostgreSQL Tables
Run the save_to_postgresql.py script to create tables and insert cleaned data:

- python scripts/save_to_postgresql.py
4. Set Up DBT
Initialize a DBT project and configure it to connect to your PostgreSQL database:

dbt init my_project
cd my_project
Update the profiles.yml(found in C/Users/your_username/.dbt) file with your PostgreSQL credentials:

my_project:
  target: dev
  outputs:
    dev:
      type: postgres
      host: your_host
      port: your_port_number
      user: your_db_user
      password: your_db_password
      dbname: your_db_name
      schema: public
      threads: 4
## Running the Pipeline
1. Data Cleaning
Run the clean_data.py script to clean the raw data:

- Follow the analysis.ipynb
2. Data Storage
Run the save_to_postgresql.py script to store the cleaned data in PostgreSQL:

- Follow the analysis.ipynb
3. DBT Transformation
Navigate to your DBT project directory and run the transformations:

dbt run
4. Testing and Documentation
Run tests and generate documentation:

dbt test
dbt docs generate
dbt docs serve

## Output
- Cleaned Data:

CSV files in the cleaned_data directory.

PostgreSQL tables: doctorset_messages, eahci_messages, lobelia4cosmetics_messages, yetenaweg_messages.

- DBT Models:

SQL models in the models directory.

Documentation available at http://localhost:8080.

- Logs:

Detailed logs in data_cleaning.log and dbt.log.

# Troubleshooting
- PostgreSQL Connection Issues:

Verify that your PostgreSQL server is running and accessible.

Double-check the connection details in .env and profiles.yml.

- DBT Errors:

Ensure the source tables exist in PostgreSQL.

Check the schema.yml file for correct source definitions.

- Data Quality Issues:

Review the logs for errors during cleaning and transformation.

Validate the data in PostgreSQL using SQL queries.


# Task 3: Object Detection Using YOLO
## Overview
Use the YOLOv5 model to detect objects in images.

Save detection results (e.g., bounding boxes, confidence scores, class labels) to a PostgreSQL database.

Log the detection process for monitoring and debugging.

## Features
Object Detection:

- Detect objects in images using YOLOv5.

- Save detection results to a PostgreSQL database.

Logging:

- Detailed logs for monitoring and debugging.

## Prerequisites
Before running the pipeline, ensure you have the following installed:

1. Python 3.9 or higher: Install Python from python.org.

2. PostgreSQL: Install PostgreSQL from postgresql.org.

3. Required Python Libraries:
Install the required libraries using the following command:

- pip install -r requirements.txt
4. YOLOv5:
Clone the YOLOv5 repository and install its dependencies:

- git clone https://github.com/ultralytics/yolov5.git
- cd yolov5
- pip install -r requirements.txt

## Setup
Just like task-2 to set up Environment Variables
Create a .env file in the root directory and add your PostgreSQL credentials:

    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_host
    DB_PORT=your_port_number

- To download images from desired telegram channels run (it save the images in ../data/images/ outside of your folder)
    - python scripts/telegram_images.py

- Don't forget to store your 
    - API_ID=your_telegram_api_id
    - API_HASH=your_telegram_api_hash
    in the .env file.
- Then follow the imgDetection_analysis.ipynb for further instructions.

# Task 4: Expose the Collected Data Using FastAPI
## Overview
Create a FastAPI application to expose the detection results via RESTful APIs.

Implement CRUD (Create, Read, Update, Delete) operations for the detection data.

Generate API documentation using Swagger UI.

## Features
FastAPI Integration:

- Expose detection results via RESTful APIs.

- Perform CRUD operations on the detection data.

Logging:

- Detailed logs for monitoring and debugging.

## Prerequisites
Before running the pipeline, ensure you have the following installed:

1. Python 3.9 or higher: Install Python from python.org.

2. PostgreSQL: Install PostgreSQL from postgresql.org.

3. Required Python Libraries:
Install the required libraries using the following command:

- pip install -r requirements.txt setup your .env just like the previous tasks(for database).

# API Endpoints
The FastAPI application exposes the following endpoints:

1. Get All Detections
Endpoint: GET /detections/

Description: Retrieve all detection results.

Example Response:

[
  {
    "id": 1,
    "image_path": "data/images/photo_2023-01-03_17-49-48.jpg",
    "class_name": "person",
    "confidence": 0.95,
    "x1": 100,
    "y1": 200,
    "x2": 300,
    "y2": 400
  }
]
2. Get Detection by ID
Endpoint: GET /detections/{detection_id}

Description: Retrieve a specific detection by ID.

Example Response:

{
  "id": 1,
  "image_path": "data/images/photo_2023-01-03_17-49-48.jpg",
  "class_name": "person",
  "confidence": 0.95,
  "x1": 100,
  "y1": 200,
  "x2": 300,
  "y2": 400
}
3. Create Detection
Endpoint: POST /detections/

Description: Create a new detection entry.

Example Request:

{
  "image_path": "data/images/photo_2023-01-03_17-49-48.jpg",
  "class_name": "person",
  "confidence": 0.95,
  "x1": 100,
  "y1": 200,
  "x2": 300,
  "y2": 400
}
4. Delete Detection
Endpoint: DELETE /detections/{detection_id}

Description: Delete a detection by ID.

# FastAPI Application
Start the FastAPI application:
    - uvicorn app.main:app --reload

## Troubleshooting
1. YOLOv5 Not Found:

- Ensure the YOLOv5 repository is cloned and added to the Python path.

- Update the sys.path.append() statement in src/main.py to point to the correct YOLOv5 directory.

2. Database Connection Issues:

- Verify that your PostgreSQL server is running and accessible.

- Double-check the connection details in .env.

3. Image Loading Errors:

- Ensure the data/images directory contains valid image files.

- Check file permissions and paths.

# AUTHOR
- Name: Natnahom Asfaw
- Date: 31/01/2025