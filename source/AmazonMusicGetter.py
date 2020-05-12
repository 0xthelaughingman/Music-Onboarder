from datetime import timedelta
from source.DriverGetterBase import DriverGetterBase
import time
import re


class AmazonMusicGetter(DriverGetterBase):
    def __init__(self, playlist_url):
        super(AmazonMusicGetter, self).__init__()
        self.asset_list = []
        self.playlist_src = playlist_url

        self.driver.get(playlist_url)
        self.find_assets()
        self.driver.quit()
        self.exec_time = timedelta(seconds=time.time() - self.exec_time)

    """
    Amazon has an interesting way to render their playlist items, probably to optimise performance.
    There's always 3 tables in the container, with each having 14 elements regardless of the actual element counts.
    As one scrolls down enough, the first table gets a Ytransform(in terms of Pixels, increments of 700) to where the elements of the 4th logical table are.
    Then the 2nd table transforms to the 5th table...and so on. Kind of a rolling/recycler view of sorts? Idk.
    """
    def find_assets(self):

        # dismiss popup about preferences since we aren't logged in
        self.move_and_click("//*[@id=\"dialogBoxView\"]/section/section/section[2]/button[2]", True)
        time.sleep(2)
        description = self.driver.find_element_by_xpath("//*[@id=\"dragonflyView\"]/div/div/div/div[2]/div[3]").get_attribute("innerHTML")
        match = re.search("(?P<count>\d+)\s*songs", description)
        total_songs = 0
        if match:
            total_songs = int(match.group("count"))
        # print(total_songs)
        total_tables = self.driver.find_elements_by_xpath(
            "//section[@class=\"playlistDetailsList noSelect\"]/div/div/table")
        # print(len(total_tables))
        cur_song_counter = 0

        # NEEDS WAY MORE TESTING, lots of possible cases.
        # One of the current issues, the loop may start before the description is rendered, leading to total_songs = 0
        while True:
            for table in range(1, len(total_tables)+1):
                table_results = self.driver.find_elements_by_xpath(
                    "//section[@class=\"playlistDetailsList noSelect\"]/div/div/table[" + str(table) + "]/tr")
                # print(len(table_results))
                for i in range(1, len(table_results)+1):
                    # Make sure the assets are rendered/in-view
                    try:
                        self.move_and_click(
                            "//section[@class=\"playlistDetailsList noSelect\"]/div/div/table[" + str(table) + "]/tr[" + str(i) + "]/td[4]", False)
                    except Exception:
                        # No more items, only ghost/recycler items.
                        break
                    tile_song = self.driver.find_element_by_xpath(
                        "//section[@class=\"playlistDetailsList noSelect\"]/div/div/table[" + str(table) + "]/tr[" + str(i) + "]/td[4]") \
                        .get_attribute("title").lower()
                    tile_artist = self.driver.find_element_by_xpath(
                        "//section[@class=\"playlistDetailsList noSelect\"]/div/div/table[" + str(table) + "]/tr[" + str(i) + "]/td[4]/span[1]/span") \
                        .get_attribute("title").lower()
                    # print(table, i, tile_artist, tile_song)
                    tile_song = self.string_normalizer(tile_song)
                    tile_artist = self.string_normalizer(tile_artist)

                    self.asset_list.append(tuple([3, tile_artist, tile_song, "Amazon Playlist"]))
                    cur_song_counter += 1
                    if cur_song_counter >= total_songs:
                        return
        return

    def get_status(self):
        log = super(AmazonMusicGetter, self).get_status()
        log = ["-"*40] + ["GetterName:" + self.__class__.__name__] + log
        return log

    def get_asset_list(self):
        return self.asset_list


if __name__ == "__main__":
    ob = AmazonMusicGetter("https://music.amazon.in/user-playlists/f64cb7bb15fc4274ab05b30e7a0dacd1i8n0?ref=dm_sh_5682-2721-4487-7bce-3f150")

    # logging
    for item in ob.get_status():
        print(item)
    # for passing onto next module
    ob.get_asset_list()
