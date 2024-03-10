from dotenv import load_dotenv
load_dotenv()

import os
from discord.ext import commands
import discord
import asyncio

# Create Discord Intents with all flags enabled
intents = discord.Intents.all()

# Create a bot instance with specified intents and command prefix
client = commands.Bot(intents=intents, command_prefix='!')

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    # Synchronize with a specific guild to decrease delay
    await client.tree.sync(guild=discord.Object(id=int(os.getenv('GUILD_ID')))) # Register for only specific guild to decrease delay

# Function to load all extensions (cogs) from the 'cogs' directory
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # Load each extension by removing the '.py' extension from the filename
            await client.load_extension(f"cogs.{filename[:-3]}")

# Main asynchronous function to run the bot
async def main():
    # Asynchronously load extensions, then start the bot with the specified token
    async with client:
        await load_extensions()
        await client.start(os.getenv('DISCORD_BOT_TOKEN'))

# Run the main function using asyncio
asyncio.run(main())
