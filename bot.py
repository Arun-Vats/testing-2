import os
from hydrogram import Client, filters
from hydrogram.types import Message
import asyncio
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Bot configuration from environment variables
API_TOKEN = os.getenv('BOT_TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

# Create the Hydrogram client
bot = Client(
    name="great_cinemas_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=API_TOKEN
)

# Welcome message handler for /start command
@bot.on_message(filters.command("start"))
async def welcome_message(client: Client, message: Message):
    """
    Handle the /start command and send a welcome message
    """
    welcome_text = (
        "🎬 Welcome to Great Cinemas Bot! 🍿\n\n"
        "Discover the world of movies and series right at your fingertips! 🌟\n\n"
        "What would you like to explore today?\n"
        "• Search for movies 🔍\n"
        "• Find series recommendations 📺\n"
        "• Get cinema info 🎥\n\n"
        "Just type your query and let the magic begin! 🌈"
    )
    
    await message.reply_text(text=welcome_text)

# Error handling and reconnection
async def keep_bot_alive():
    while True:
        try:
            await bot.start()
            logger.info("Bot started successfully!")
            await bot.idle()
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            logger.info("Attempting to restart the bot...")
            await asyncio.sleep(5)

# Main function
def main():
    logger.info("Great Cinemas Bot is starting...")
    asyncio.run(keep_bot_alive())

if __name__ == "__main__":
    main()
