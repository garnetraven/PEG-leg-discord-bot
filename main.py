from dotenv import load_dotenv
load_dotenv()

import os
import discord
from discord.ext import commands

client = commands.Bot(
    intents=discord.Intents.all(),
    command_prefix='!'
)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # register application command tree with Discord 
    await client.tree.sync(guild=discord.Object(id=int(os.getenv('GUILD_ID')))) # register for only specific guild to decrease delay

# EXAMPLE: OLD PREFIX COMMAND
@client.command()
async def prefixtest(ctx: commands.Context):
    await ctx.channel.send(f'Hi {ctx.author.name}! Welcome to {ctx.guild.name}.')

# EXAMPLE: SLASH COMMAND
@client.tree.command(
    name='slashtest',
    description='A test slash command',
    guild=discord.Object(id=int(os.getenv('GUILD_ID'))) # register for only specific guild to decrease delay
)
async def slashtest(interaction: discord.interactions.Interaction):
    await interaction.response.send_message(f'Hi {interaction.user.name}! Welcome to {interaction.guild.name}.')

client.run(os.getenv('DISCORD_BOT_TOKEN'))
