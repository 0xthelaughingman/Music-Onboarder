from datetime import timedelta
from source.DriverSetterBase import DriverSetterBase
import time
from selenium.webdriver.common.action_chains import ActionChains
from source.FuzzyMatcher import FuzzyMatcher


class SpotifySetter(DriverSetterBase):

    def __init__(self, test_mode=False, asset_list=list, email=None, password=None, playlist_name=None):
        super(SpotifySetter, self).__init__()
        self.login(test_mode, email, password)
        self.setup_playlist(playlist_name)
        self.asset_list = asset_list
        self.status_matched = []
        self.status_failed = []
        self.find_assets(self.asset_list)
        self.driver.quit()
        self.exec_time = timedelta(seconds=time.time() - self.exec_time)
        self.log_status()

    def login(self, test_mode, email, password):
        self.driver.get('https://open.spotify.com/')

        if test_mode is False or (email is None or password is None):
            print("Please Sign in to the service.\n")
            while True:
                res = input("Press y/Y to continue after sign-in...\n")
                if res == 'y' or res == 'Y':
                    break
        else:
            self.password = password
            self.email = email
            self.move_and_click("//*[@id=\"main\"]/div/div[3]/div[1]/header/div[4]/button[2]", True)
            self.driver.find_element_by_xpath("//*[@id=\"login-username\"]").send_keys(self.email)
            self.driver.find_element_by_xpath("//*[@id=\"login-password\"]").send_keys(self.password)
            self.move_and_click("//*[@id=\"login-button\"]", True)

    def setup_playlist(self, playlist):
        if playlist is None:
            self.playlist_name = input("Enter the new playlist name...\n")
        else:
            self.playlist_name = playlist

        self.move_and_click("//button/span[text()=\"Create Playlist\"]", True)
        self.driver.find_element_by_xpath(
            "//*[@id=\"main\"]/div/div[4]/div/div[1]/div/div/input").send_keys(self.playlist_name)
        self.move_and_click("//*[@id=\"main\"]/div/div[4]/div/div[2]/div[2]/button", True)

    # Method to handle the adding of selected tile asset to playlist
    def add_tile_asset(self, target_tile: int):

        # Making sure with move_to to the Artist/Title name that the context menu is visible for that tile
        self.move_and_click(
            "//*[@id=\"searchPage\"]/div/div/section[2]/div/div[2]/div[" + str(target_tile) + "]/div/div/div[3]/a",
            False)

        # click context menu
        self.context_click(
            "//*[@id=\"searchPage\"]/div/div/section[2]/div/div[2]/div[" + str(target_tile) + "]/div/div/div[3]/a")

        # Add to playlist
        self.move_and_click("//*[@id=\"main\"]/div/nav[1]/div[4]", True)
        # iterate through playlists to find our playlist
        time.sleep(1)
        playlists = results = self.driver.find_elements_by_xpath(
            "//*[@id=\"main\"]/div/div[4]/div/div[2]/div/div")
        # print("playlist len: ", len(playlists))

        # Leads to an exception at times as the playlist dialog never opens up at times...
        playlist_loc = 1
        for i in range(1, min(len(playlists)+1, 5)):
            cur_playlist = self.driver.find_element_by_xpath(
                "//*[@id=\"main\"]/div/div[4]/div/div[2]/div/div[" + str(i) + "]/div/div/div/div/div/div[2]/div/div") \
                .text
            # print("Current Playlist= ", cur_playlist)
            if cur_playlist == self.playlist_name:
                playlist_loc = i
                break
        # print("playlist loc: ", playlist_loc)
        # Making sure playlist visible
        self.move_and_click(
            "//*[@id=\"main\"]/div/div[4]/div/div[2]/div/div[" + str(playlist_loc) + "]/div/div/div/div/div/div[1]/div",
            True)

    # Method for handling the searching of an asset, returns the number of tiles available after the search
    def search_asset(self, artist, title):
        # click the search button to transition to the search page
        time.sleep(2)
        self.move_and_click("//*[@id=\"main\"]/div/div[3]/div[2]/nav/ul/li[2]/div/a/div/div[3]", True)

        search_area = self.driver.find_element_by_xpath(
            "//*[@id=\"main\"]/div/div[3]/div[1]/header/div[3]/div/div/label/input"
        )
        ActionChains(self.driver).move_to_element(search_area).click(search_area).perform()
        search_area.clear()
        search_area.send_keys(artist + " " + title)

        # results auto populate after entering, no actions needed to search

        results = self.driver.find_elements_by_xpath(
            "//*[@id=\"searchPage\"]/div/div/section[2]/div/div[2]/div/div")

        return results

    # The method that iterates through assets, searching the asset and adding to playlist if found as a Match.
    def find_assets(self, asset_list):
        # testing
        if asset_list is None:
            asset_list = [(3, "alan walker", "force"),
                          (2, "siafugasudfgsidfg", "asudgausgdausydg"),
                          (3,  "ahrix", "nova"),
                          (3, "alan walker", "spectre")
                          ]

        for asset in asset_list:
            asset_filetype = asset[0]
            if asset_filetype == 0:
                self.status_failed.append("FILE FAILED=" +str(asset))
                continue
            asset_artist = asset[1]
            asset_title = asset[2]

            results = self.search_asset(asset_artist, asset_title)
            # print(len(results))
            # Expected to handle an exception for this case...but this seems to work somehow...
            if len(results) == 0:
                self.status_failed.append("NO RESULTS=" + str(asset))
                continue

            # iterate result tiles and match, max attempts = 5
            found = 0
            max_factor = 0
            target_tile = 0
            for i in range(1, min(len(results)+1, 5)):
                tile_song = self.driver.find_element_by_xpath(
                    "//*[@id=\"searchPage\"]/div/div/section[2]/div/div[2]/div[" + str(i) + "]/div/div/div[3]/a")\
                    .text.lower()
                tile_artist = self.driver.find_element_by_xpath(
                    "//*[@id=\"searchPage\"]/div/div/section[2]/div/div[2]/div[" + str(i) + "]/div/div/div[3]/div/span/a")\
                    .text.lower()
                # Match condition, needs a proper handler class with advanced logic/fuzzy....
                current_factor = FuzzyMatcher.get_match_factor(asset_filetype, asset_artist, asset_title, tile_artist, tile_song)
                # print(asset_title, asset_artist, "VS", tile_song, tile_artist, current_factor)
                if current_factor > max_factor:
                    target_tile = i
                    max_factor = current_factor

            if max_factor != 0:
                found = 1

            if found == 1:
                try:
                    self.add_tile_asset(target_tile)
                    self.status_matched.append(
                        "MATCH SUCCESS=" + str(asset) + " | " + "MATCH FACTOR=" + str(max_factor))
                    time.sleep(1)
                except Exception as e:
                    print(e)
                    self.status_failed.append("FAILED TO ADD DUE TO EXCEPTION=" + str(asset))
            else:
                self.status_failed.append("FAILED TO MATCH=" + str(asset))


if __name__ == "__main__":
    ob = SpotifySetter(False)

