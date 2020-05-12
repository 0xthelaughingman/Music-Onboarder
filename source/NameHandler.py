"""
The objective of this module is to yield a tuple containing info about:
-Quality of the file and metadata.
-Metadata such as the Artist and Title of the song, as available
"""
import re
from mutagen.easyid3 import EasyID3

file_quality = [
    3,  # The file has good metadata/tags.
    2,  # The file had poor metadata but info derivable from file_name
    1,  # The file is bad, using the whole name as backup.
    0   # Bad File/Error in handling the file
]


class NameHandler:
    re_pattern = "^(?P<artist>.*)\s*-\s*(?P<title>.*)\."
    file_list = []
    asset_pair =[]

    def __init__(self, file_list):
        self.file_list = file_list

    def get_file_metadata(self, filepath):
        try:
            d = EasyID3(filepath)
            # title = d['title'][0].lower()
            for item in d['title']:
                title = " " + item.lower()
            # artist = d['artist'][0].lower()
            for item in d['artist']:
                artist = " " + item.lower()
            # print(title + " ### " + artist)
            return [file_quality[0], artist, title]

        except Exception:
            # print("BAD METADATA ::" + filepath)
            return None

    def get_file_name(self, filepath):

        file_name = filepath.split("/")
        # print(file_name)
        file_name = file_name[len(file_name)-1]
        match = re.search(self.re_pattern, file_name)
        if match:
            return [file_quality[1], match.group("artist").strip().lower(), match.group("title").strip().lower()]

        # No distinction of artist/title, just send the whole filename...
        match2 = re.search("(?P<file_name>.*)\.", file_name)
        if match2:
            return [file_quality[2], match2.group("file_name").strip().lower(), None]

        return [file_quality[3], "BAD FILE :: " + file_name]

    # Here after, we want the file data to be immutable!
    def clean_strings(self, data):
        # print(data)
        re_urls = "\[?\(?[a-z0-9]+([\-_\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?\)?\]?"
        re_bitrates = "[\(\[]?\d*\s*kbps[\)\]]?"
        re_vid_keywords = "[\(\[]?\w+ video[\)\]]?|\d+p"
        re_feats = "ft\.|featuring\."
        re_brackets_etc = "\(|\[|\]|\)"
        re_spaces = "\s\s+"
        # No hope for this file!
        if data[0] == 0:
            return tuple(data)
        """
        Maintain the hierarchy of the substitutions, else the strings might break.
        """
        for n in range(1, len(data)):
            if data[n]:
                data[n] = re.sub(re_urls, "", data[n])
                data[n] = re.sub(re_bitrates, "", data[n])
                data[n] = re.sub(re_vid_keywords, "", data[n])
                data[n] = re.sub(re_feats, "feat.", data[n])
                data[n] = re.sub(re_brackets_etc, " ", data[n])
                data[n] = re.sub(re_spaces, " ", data[n])
                data[n] = data[n].strip()
        # print(tuple(data))
        return tuple(data)

    def set_pairs(self):
        for fpath in self.file_list:

            # Primary attempt to extract Artist/Title
            data_list = self.get_file_metadata(fpath)

            # Backup, from the file name...
            if data_list is None:
                data_list = self.get_file_name(fpath)

            data_tuple = self.clean_strings(data_list)

            self.asset_pair.append(data_tuple)

    def get_pairs(self):
        self.set_pairs()
        return self.asset_pair


if __name__ == "__main__":
    sample = [
              'Arctic Monkeys - I Wanna Be Yours.mp3',
              'Arctic Monkeys - One For The Road Official Video[www.MP3Fiber.com].mp3',
              'Arctic Monkeys - R U Mine.mp3',
              'Arctic Monkeys By Stop The World I Wanna Get Off With You Official Audio[www.MP3Fiber.com].mp3'
              ]
    ob = NameHandler(sample)
    for i in ob.get_pairs():
        print(i)