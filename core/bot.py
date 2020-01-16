from discord import Client as DiscordClient
from .message import process_message
from .guild import Guild

class Client(DiscordClient):
    async def on_ready(self):
        self.print_connected_guilds()

    async def on_message(self, message):
        """Event on_message from the client Discord"""
        channel = message.channel
        guild = message.guild

        Guild(uid=guild.id, name=guild.name).process_guild()
        response = process_message(message)

        if self.is_my_message(message):
            return

        await channel.send(response) 

    def print_connected_guilds(self) -> None:
        """Print the list of the connected guilds"""
        print(self.user)

        for guild in self.guilds:
            print(f'Connected to {guild.name}: {guild.id}')

    def is_my_message(self, message):
        return message.author.id == self.user.id