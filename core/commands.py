from core.mettings import StandUpMetting, finish_metting
from discord.message import Message as DiscordMessage

commands = {
    "start": {
        "dsm": StandUpMetting.start_from_message
    },
    "finish": finish_metting, 
}

class Command:
    commands = commands

    def __init__(self, args: list, message: DiscordMessage):
        self.args = args
        self.message = message
        
    def is_valid(self) -> bool:
        """check if command passed is valid"""
        if self._get_command():
            return True

        return False

    def _get_command(self):
        """try to find a command for the passeds args"""
        command = self.commands

        try:
            for arg in self.args:
                command = command[arg]
                if callable(command):
                    return command
        except KeyError:
            pass   

    def execute(self):
        assert self.is_valid()
        command = self._get_command()

        return command(self.args, self.message)