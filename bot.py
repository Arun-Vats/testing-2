from hydrogram import Client, filters
from hydrogram.types import Message

# Bot configuration
API_TOKEN = "6560753033:AAGH7ovYYXR7UmCeWUNuYQBjirlaLQ3ItLc"  # Get from BotFather
API_ID = 11834008  # Replace with your actual numeric API ID
API_HASH = "469c11d445ed952818017329db22483f"  # Replace with your actual API Hash

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
    
    await message.reply_text(
        text=welcome_text
    )

# Run the bot
def main():
    print("Great Cinemas Bot is starting...")
    bot.run()

if __name__ == "__main__":
    main()