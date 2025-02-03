from telethon import TelegramClient
import os
from  dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient('telegram_coll_images', api_id, api_hash)

image_dir = 'data/images'
os.makedirs(image_dir, exist_ok=True)

async def fetch_images(channel):
    async for message in client.iter_messages(channel):
        if message.photo:
            photo = await message.download_media(file=image_dir)
            print(f'Downloaded: {photo}')

async def main():
    await client.start()
    await fetch_images('@CheMed123')  # Replace with your channel username
    await fetch_images('@lobelia4cosmetics')  # Replace with your channel username

with client:
    client.loop.run_until_complete(main())