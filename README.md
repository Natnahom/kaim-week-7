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

