import os
import logging
import pandas as pd
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetHistoryRequest
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="telegram_scraping.log"
)

# Telegram API credentials
# Access the variables for api credentials
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

# Output directory for raw data
RAW_DATA_DIR = "raw_data"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# Initialize Telegram client
client = TelegramClient("telegram_data_scraper", API_ID, API_HASH)

# Function to fetch messages from a Telegram channel
async def fetch_messages(channel_username, limit=100):
    """
    Fetch messages from a Telegram channel.
    
    Args:
        channel_username (str): Username of the Telegram channel.
        limit (int): Number of messages to fetch.
    
    Returns:
        list: List of messages with metadata.
    """
    try:
        logging.info(f"Fetching messages from {channel_username}")
        channel = await client.get_entity(channel_username)
        messages = await client(GetHistoryRequest(
            peer=channel,
            limit=limit,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0
        ))
        await asyncio.sleep(2)  # Add a 2-second delay between requests
        return messages.messages
    except Exception as e:
        logging.error(f"Error fetching messages from {channel_username}: {e}")
        return []

# Function to save messages to a CSV file
def save_to_csv(messages, channel_name):
    """
    Save scraped messages to a CSV file.
    
    Args:
        messages (list): List of messages with metadata.
        channel_name (str): Name of the Telegram channel.
    """
    try:
        data = []
        for message in messages:
            data.append({
                "id": message.id,
                "date": message.date,
                "message": message.message,
                "views": message.views if hasattr(message, "views") else None,
                "media": bool(message.media)
            })
        
        df = pd.DataFrame(data)
        file_path = os.path.join(RAW_DATA_DIR, f"{channel_name}_messages.csv")
        df.to_csv(file_path, index=False)
        logging.info(f"Saved {len(data)} messages to {file_path}")
    except Exception as e:
        logging.error(f"Error saving messages to CSV: {e}")

# Main function to scrape and save data
async def scrape_telegram_channel(channel_username, limit=100):
    """
    Scrape messages from a Telegram channel and save them to a CSV file.
    
    Args:
        channel_username (str): Username of the Telegram channel.
        limit (int): Number of messages to fetch.
    """
    messages = await fetch_messages(channel_username, limit)
    if messages:
        save_to_csv(messages, channel_username)

# List of Telegram channels to scrape
CHANNELS = [
    "@DoctorsET",
    "@Chemed",
    "@lobelia4cosmetics",
    "@yetenaweg",
    "@EAHCI"
]

# Run the scraper
async def main():
    await client.start(PHONE_NUMBER)
    logging.info("Client started successfully. Beginning scraping...")  # Debug log
    for channel in CHANNELS:
        await scrape_telegram_channel(channel, limit=100)
    await client.disconnect()

# Execute the script
if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())