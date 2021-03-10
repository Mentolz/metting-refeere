from discord.message import Message as DiscordMessage
from core.commands import Command

def process_message(message: DiscordMessage) -> str:
    if message.content.startswith('lex'):
        args = message.content.split()[1:]
        
        command = Command(args, message)
        if command.is_valid():
            return command.execute()
        
        return False