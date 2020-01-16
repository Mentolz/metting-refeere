import os
from settings import base as settings
import json 

class Guild:
    _base_path = settings.GUILD_PATH

    def __init__(self, uid, name):
        self.uid = str(uid)
        self.name = name
        self.path = self._base_path + "/" + self.uid

    @property
    def info_dict(self) -> dict:
        return {
            "uid": self.uid,
            "name": self.name,
        }

    def process_guild(self):
        if not self.is_registed():
            self.regist()

    def is_registed(self) -> bool:
        """Check if there is a directory to store the guild information"""
        return os.path.exists(self.path)

    def regist(self):
        """Create a directory to store guild information and a file 
        with the correspondent private data of the guild
        """

        os.makedirs(self.path)
        with open(f"{self.path}/info.json", "w") as info_file:
            json.dump(self.info_dict, info_file)
        