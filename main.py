from dotenv import load_dotenv
load_dotenv()

import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix='!')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.tree.sync(guild=discord.Object(id=int(os.getenv('GUILD_ID'))))

# Load the PDFConverter cog
client.load_extension('pdf_converter')

client.run(os.getenv('DISCORD_BOT_TOKEN'))
