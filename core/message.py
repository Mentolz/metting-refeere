from discord.message import Message as DiscordMessage

def process_message(message):
    if message.content.startswith('Ambrosio'):
        return f'Olá {message.author.name}, apetece-lhe algo?'