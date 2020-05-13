
from source.AmazonMusicSetter import AmazonMusicSetter
from source.AmazonMusicGetter import AmazonMusicGetter
from source.DirHandler import DirHandler
from source.NameHandler import NameHandler
from source.SpotifySetter import SpotifySetter
from source.SpotifyGetter import SpotifyGetter
import time
from source.utils.loggerHelper import LoggingHelper


if __name__ == "__main__":
    logger_def = LoggingHelper.setup_logger()
    ob = AmazonMusicGetter("https://music.amazon.in/user-playlists/24c50364686646d29c50c237d7abf1f8i8n0?ref=dm_sh_5f15-f02c-7958-1c3b-b801b")
    ob = SpotifySetter(True, ob.get_asset_list(), "email", "password", "TEST")


