import time
from datetime import timedelta
from source.DriverGetterBase import DriverGetterBase


class SpotifyGetter(DriverGetterBase):

    def __init__(self, playlist_url):
        super(SpotifyGetter, self).__init__()
        self.asset_list = []
        self.playlist_src = playlist_url

        self.driver.get(playlist_url)
        self.find_assets()
        self.driver.quit()
        self.exec_time = timedelta(seconds=time.time() - self.exec_time)
        self.log_status()

    def find_assets(self):
        results = self.driver.find_elements_by_xpath(
            "//ol[@class=\"tracklist\"]/div")

        for i in range(1, len(results)+1):
            tile_song = self.driver.find_element_by_xpath(
                "//ol[@class=\"tracklist\"]/div[" + str(i) + "]/div/li/div[2]/div/div[1]") \
                .text.lower()

            # This row might contain 'E' symbol & others before the artist name's span which doesn't have an anchor...
            # Hence, trying to find the first relative /span/span/span/a's text
            tile_artist = self.driver.find_element_by_xpath(
                "//ol[@class=\"tracklist\"]/div[" + str(i) + "]/div/li/div[2]/div/div[2]/span/span/span/a") \
                .text.lower()
            tile_song = self.string_normalizer(tile_song)
            tile_artist = self.string_normalizer(tile_artist)
            self.logger.debug(
                str("Current Song : %s - %s" % (tile_song, tile_artist)))
            self.asset_list.append(tuple([3, tile_artist, tile_song, "Spotify Playlist"]))

        return


if __name__ == "__main__":
    ob = SpotifyGetter("https://open.spotify.com/playlist/2skhgmWPS9RicUbXYgpAKh?si=P_7Aq3lhQkS6TKNVWV7GBQ")
    # for passing onto next module
    ob.get_asset_list()
