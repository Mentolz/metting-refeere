from core.guild import Guild
from discord.member import Member as DiscordMember
from typing import List


class Metting:
    type_ = str()

    def __init__(self, participants: List[DiscordMember], guild: Guild):
        self.participants = participants
        self.guild = guild

    @property
    def participants_number(self):
        return len(self.participants)

    @property
    def type(self):
        return self.type_

    @classmethod
    def start_from_message(cls, args, message):
        metting = cls(message.channel.members, message.channel.guild)
        minutes = args[2]
        return metting.start(minutes)

    def start(self, time):
        return f"Started Daily Stand-up Metting with {len(self.participants)} participants. Each one has {time} minutes to talk"


class StandUpMetting(Metting):
    type_ = "Stand-Up Metting"



class SprintPlanningMetting(Metting):
    type_ = "Sprint Planning Metting"


def finish_metting(metting):
    return "Metting Finished"