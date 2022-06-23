'''
Simple SSH manager to log into your 
remote servers in one click

Author: Adarsh Punj
June 2022
'''

from utils import __preferences__ as prf

from dataclasses import dataclass
import subprocess
import json
import os

import rumps

@dataclass
class ServerModel:

	server_name: str
	username: str
	ip: str
	key_location: str

	@property
	def ssh_command(self) -> str:
		return f"sudo ssh -i '{self.key_location}' {self.username}@{self.ip}"

class SshManagerApp(rumps.App):

    """
    rumps.App
    """

    def __init__(self):
        super(SshManagerApp, self).__init__(name="SSH Manager")

        self.title = "ssʜ"

        self.menu = [
            *self.menu_list,
            None,
            rumps.MenuItem('Manage servers...',callback=self.edit_preferences)
            ]

    @property
    def menu_list(self) -> list:

        '''
        Returns a list of rumps.MenuItem objects
        from a list of dictionaries
        '''
        _server_list = self._server_list

        return [

            rumps.MenuItem(
                ServerModel(**x).server_name
                , callback=self.exec_ssh_command_by_server_name

                ) for x in _server_list
            ]

    @classmethod
    def exec_ssh_command_by_server_name(self, sender, sound=prf.PLAY_SOUND) -> None:

        for item in prf.AVAILABLE_SERVERS:
            server = ServerModel(**item)
            subprocess.run(
                ['osascript','-e',f'tell app "Terminal" to do script ("{server.ssh_command}")']
            ) if server.server_name == sender.title.strip() else None

            if sound:
                subprocess.run(['afplay',prf.DEFAULT_SOUND])

    @classmethod
    def edit_preferences(self, sender) -> None:

        subprocess.run(
            ['open','./preferences.json']
        )


    @property
    def _server_list(self) -> [dict]:
        return prf.AVAILABLE_SERVERS

if __name__ == '__main__':
    SshManagerApp().run()