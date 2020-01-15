import os

import discord
from dotenv import load_dotenv
from utils import print_connected_guilds

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print_connected_guilds(client)

@client.event
async def on_message(message):
    if message.content.startswith('Ambrosio'):
        channel = message.channel
        await channel.send(f'Olá {message.author.name}, apetece-lhe algo?') 

client.run(TOKEN)