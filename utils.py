from discord import Client
 

def print_connected_guilds(client: Client) -> None:
    """Print the list of the connected guilds"""
    print(f'{client.user} is connected to the following guild:')
    
    for guild in client.guilds:
        print(f'{guild.name}(id: {guild.id})') 