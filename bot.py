import discord
import os
from discord.ext import commands

# Replace "PREFIX" with your preferred bot's prefix.
client = commands.Bot(command_prefix='PREFIX')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Replace "TOKEN" with your bot's discord token.
client.run('TOKEN')
