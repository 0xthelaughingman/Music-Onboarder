"""
Module to run the user's selected scenario.

"""

from source.SpotifyGetter import SpotifyGetter
from source.AmazonMusicGetter import AmazonMusicGetter
from source.AmazonMusicSetter import AmazonMusicSetter
from source.SpotifySetter import SpotifySetter
from source.DirHandler import DirHandler
from source.NameHandler import NameHandler
from source.utils.loggerHelper import LoggingHelper


class Orchestrator:

    def __init__(self, src_type: str, src_url: str, dest_type: str):
        LoggingHelper.setup_logger()
        self.src_type = src_type
        self.src_url = src_url
        self.dest_type = dest_type

        self.run_driver_getter()
        self.run_driver_setter()

        return

    def run_driver_setter(self):

        if self.dest_type == "spotify":
            SpotifySetter(False, self.playlist)

        if self.dest_type == "amazon":
            AmazonMusicSetter(False, self.playlist)

        return

    def run_driver_getter(self):

        if self.src_type == "local directory":
            file_names = DirHandler(self.src_url).get_files()
            self.playlist = NameHandler(file_names).get_pairs()

        if self.src_type == "spotify":
            self.playlist = SpotifyGetter(self.src_url).get_asset_list()

        if self.src_type == "amazon":
            self.playlist = AmazonMusicGetter(self.src_url).get_asset_list()

        return


if __name__ == "__main__":
    # ob = Orchestrator("spotify", "https://open.spotify.com/playlist/59WRCXz7aEqBHqyTfQt479?si=ghjtB4XwTe6foXh5UNgB6Q", "amazon")
    ob = Orchestrator("amazon", "https://music.amazon.in/user-playlists/f64cb7bb15fc4274ab05b30e7a0dacd1i8n0?ref=dm_sh_8723-fe71-e54e-0153-49b2d", "spotify")