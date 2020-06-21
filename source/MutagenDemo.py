"""
Module to experiment with Mutagen and the metadata ID3 tags! :)

"""

from mutagen.easyid3 import EasyID3
import os

file_list = []

for file in os.listdir("path"):
    if file.endswith(".mp3") or file.endswith(".mp4"):
        # file = file.replace("_", " ")
        file_list.append("path" + file)

for i in file_list:

    try:
        d = EasyID3(i)
        title = d['title'][0]
        artist = d['artist'][0]
        print(title + " ### " + artist)
    except Exception:
        print("File ::" + i)