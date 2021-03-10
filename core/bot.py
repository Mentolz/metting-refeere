from discord import Client as DiscordClient
from .message import process_message
from .guild import Guild

class Client(DiscordClient):
    async def on_ready(self):
        self.print_connected_guilds()

    async def on_message(self, message):
        """Event on_message from the client Discord"""
        if self.is_my_message(message):
            return

        channel = message.channel
        response = process_message(message)

        if response is False:
            await channel.send(
                f"Sorry {message.author.name}, the command wasn't found"
            )

        if response:
            await channel.send(response) 

        return

    def print_connected_guilds(self) -> None:
        """Print the list of the connected guilds"""
        print(self.user)

        for guild in self.guilds:
            print(f'Connected to {guild.name}: {guild.id}')

    def is_my_message(self, message):
        return message.author == self.user
        
    def on_guild_join(self, guild):
        Guild(uid=guild.id, name=guild.name).process_guild()
