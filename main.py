from dotenv import load_dotenv
load_dotenv()

import os
from discord.ext import commands
import discord
import asyncio

intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix='!')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.tree.sync(guild=discord.Object(id=int(os.getenv('GUILD_ID')))) # register for only specific guild to decrease delay


@client.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load_extensions()
        await client.start(os.getenv('DISCORD_BOT_TOKEN'))

asyncio.run(main())