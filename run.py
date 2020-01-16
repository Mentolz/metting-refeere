from core.bot import Client
from settings import base as settings

client = Client()
client.run(settings.DISCORD_TOKEN)