import re
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeDriverAmazonMusic:
    driver = None
    playlist_name = None
    asset_list = None
    status = None
    # only for testing
    email = "email"
    password = "password"

    def __init__(self, test_mode=False, email=None, password=None, playlist=None, asset_list=None):

        # Only supporting win/Mac OS X
        if sys.platform == "win32":
            self.driver = webdriver.Chrome('./webdriver/chromedriver.exe')
        else:
            self.driver = webdriver.Chrome('./webdriver/chromedriver_mac64')
        # Primary page should be 'music.amazon.com', '.in' just to ease testing, otherwise 2 hops of log-ins
        self.driver.implicitly_wait(10)
        self.driver.get('https://music.amazon.in/')
        if test_mode is False:
            print("Please Sign in to the service.\n")
            while True:
                res = input("Press y/Y to continue after sign-in...\n")
                if res == 'y' or res == 'Y':
                    break
        else:
            self.password = password
            self.email = email
            self.driver.find_element_by_xpath("//*[@id=\"dialogBoxView\"]/section/section/section[2]/button[2]").click()
            self.driver.find_element_by_xpath("//*[@id=\"contextMenu\"]/li[1]/a").click()
            self.driver.find_element_by_xpath("//*[@id=\"ap_email\"]").send_keys(self.email)
            self.driver.find_element_by_xpath("//*[@id=\"ap_password\"]").send_keys(self.password)
            self.driver.find_element_by_xpath("//*[@id=\"signInSubmit\"]").click()

        self.setup_playlist(playlist)
        self.asset_list = asset_list
        self.status =[]
        self.find_assets(self.asset_list)
        self.driver.quit()

    def setup_playlist(self, playlist):
        if playlist is None:
            self.playlist_name = input("Enter the new playlist name...\n")
        else:
            self.playlist_name = playlist
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id=\"newPlaylist\"]").click()
        self.driver.find_element_by_xpath("//*[@id=\"newPlaylistName\"]").send_keys(self.playlist_name)
        self.driver.find_element_by_xpath("//*[@id=\"savePlaylistDialog\"]/a").click()

    def find_assets(self, asset_list):
        # testing
        if asset_list is None:
            asset_list = ["alan walker-force", "siafugasudfgsidfg-asudgausgdausydg", "ahrix-nova", "alan walker-spectre"]
            #asset_list = ["siafugasudfgsidfg-asudgausgdausydg"]
        for asset in asset_list:
            asset_group = asset.split("-")
            asset_artist = asset_group[0]
            asset_song = asset_group[1]
            if asset_artist == "INVALID FILENAME":
                self.status.append("FAILED :: ")
                continue

            # print(asset_song, asset_artist)
            # Making sure with move_to that the element is visible/interactable
            search_area = self.driver.find_element_by_xpath("// *[ @ id = \"searchMusic\"]")
            ActionChains(self.driver).move_to_element(search_area).click(search_area).perform()
            search_area.clear()
            search_area.send_keys(asset_artist + " " + asset_song)

            self.driver.find_element_by_xpath("//*[@id=\"dragonflyTransport\"]/div/div[1]/div/button").click()
            self.driver.find_element_by_xpath("//*[@id=\"dragonflyTransport\"]/div/div[1]/div/button").click()

            results = self.driver.find_elements_by_xpath(
                "//*[@id=\"dragonflyView\"]/div/div[2]/div[2]/section/section[3]/div[2]/div/div[1]/div")

            # Expected to handle an exception for this case...but this seems to work somehow...
            if len(results) == 0:
                self.status.append("NO RESULTS :: " + asset)
                continue

            # iterate result tiles and match, max attempts = 5
            found = 0
            i = 0
            for i in range(1, min(len(results), 5)):
                tile_song = self.driver.find_element_by_xpath(
                    "//*[@id=\"dragonflyView\"]/div/div[2]/div[2]/section/section[3]/div[2]/div/div[1]/div[" + str(i) + "]/div[2]/div[1]").get_attribute("title").lower()

                tile_artist = self.driver.find_element_by_xpath(
                    "//*[@id=\"dragonflyView\"]/div/div[2]/div[2]/section/section[3]/div[2]/div/div[1]/div[" +
                    str(i) + "]/div[2]/div[2]").get_attribute("title").lower()
                print(asset_song, asset_artist, "VS", tile_song, tile_artist)
                # Match condition, needs a proper handler class with advanced logic/fuzzy....
                if (tile_song == asset_artist and tile_artist == asset_song) or (tile_song == asset_song and tile_artist == asset_artist):
                    self.driver.find_element_by_xpath("//*[@id=\"dragonflyView\"]/div/div[1]/div/h1").click()

                    # Making sure with move_to that the element is visible/interactable
                    button = self.driver.find_element_by_xpath(
                        "//*[@id=\"dragonflyView\"]/div/div[2]/div[2]/section/section[3]/div[2]/div/div[1]/div[" + str(i) + "]/div[3]/span[3]")
                    ActionChains(self.driver).move_to_element(button).click(button).perform()
                    self.driver.find_element_by_xpath("//*[@id=\"contextMenuContainer\"]/section/ul/li[2]/div").click()
                    self.driver.find_element_by_xpath(
                        "//dl/dd/ul/li/span[contains(text(), '" + self.playlist_name + "')]").click()

                    found = 1
                    time.sleep(5)
                    break

            if found == 1:
                self.status.append("MATCH SUCCESS :: " + asset)

            else:
                self.status.append("FAILED TO MATCH :: " + asset)

    def get_status(self):
        return self.status


if __name__ == "__main__":
    ob = ChromeDriverAmazonMusic(True, "Testing")
    print(ob.status)
