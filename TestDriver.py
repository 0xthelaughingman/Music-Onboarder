from datetime import timedelta
from source.AmazonMusicSetter import AmazonMusicSetter
from source.AmazonMusicGetter import AmazonMusicGetter
from source.DirHandler import DirHandler
from source.NameHandler import NameHandler
from source.SpotifySetter import SpotifySetter
from source.SpotifyGetter import SpotifyGetter
import time


# file_names = DirHandler("path").get_files()
# asset_list = NameHandler(file_names).get_pairs()
# Update details as needed
# print(asset_list)
# ob = AmazonMusicSetter(True, "email", "pass", "Testing", asset_list)


start = time.time()
ob = AmazonMusicGetter("https://music.amazon.in/user-playlists/24c50364686646d29c50c237d7abf1f8i8n0?ref=dm_sh_5f15-f02c-7958-1c3b-b801b")

results = ob.get_status()
for i in results:
    print(i)

ob = SpotifySetter(True, "email", "password", "Pop 2020", ob.get_asset_list())
'''
ob = SpotifyGetter("https://open.spotify.com/playlist/7nrSuqa9SQ18XTgwFKD6gG?si=V3w4_rsgTNqTNDGxM4IKWw")
ob = AmazonMusicSetter(True, "email", "password", "ETE", ob.get_asset_list())
'''
# ob = SpotifySetter(True, "email", "pass", "Testing")

results = ob.get_status()
for i in results:
    print(i)


exec_time = timedelta(seconds=time.time()-start)
print("Overall Time : ", exec_time)