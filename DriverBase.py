"""
Base class for all supported services' Drivers.
Important Notes:
The drivers are currently designed to be able to run as standalone modules to assist in testing.
sub class init prototype:(self, test_mode=False, email=None, password=None, playlist=None, asset_list=None)

As such, the sub class constructors are expected to allow the following legal usage/param combinations:
-(self, test_mode=False) -> For a mock user case, where the user inputs the required params.

-(self, test_mode=True, email, password) ->Where the login is automated, playlist and assets
are default test configs.

-(self, test_mode=False, email, password, playlist, asset_list) -> ETE case,
as is expected to be run from the app once the prerequisites are already collected in a separate module

"""

import sys
from selenium import webdriver
from selenium.webdriver import ActionChains


class DriverBase:
    driver = None
    playlist_name = None
    asset_list = None
    status_matched = None
    status_failed = None

    def __init__(self):
        # Only supporting win/Mac OS X
        if sys.platform == "win32":
            self.driver = webdriver.Chrome('./webdriver/chromedriver.exe')
        else:
            self.driver = webdriver.Chrome('./webdriver/chromedriver_mac64')
        self.driver.implicitly_wait(10)

    # Method for easy clicking/ just movement to the element as per the bool flag
    def move_and_click(self, xpath: str, click: bool):
        element = self.driver.find_element_by_xpath(xpath)
        if click is True:
            ActionChains(self.driver).move_to_element(element).click().perform()
        else:
            ActionChains(self.driver).move_to_element(element).perform()

    def context_click(self, xpath: str):
        element = self.driver.find_element_by_xpath(xpath)
        ActionChains(self.driver).move_to_element(element).context_click().perform()


    def setup_playlist(self, playlist):
        return

    # Method to handle the adding of selected tile asset to playlist
    def add_tile_asset(self, target_tile: int):
        return

    # Method for handling the searching of an asset, returns the number of tiles available after the search
    def search_asset(self, artist, title):
        return

    # The method that iterates through assets, searching the asset and adding to playlist if found as a Match.
    def find_assets(self, asset_list):
        return

    def get_status(self):
        matched = len(self.status_matched)
        failed = len(self.status_failed)
        total = matched + failed
        match_rate = round(matched/total * 100, 2)

        log = []
        summary = "Total=" + str(total) + ", Matches=" + str(matched) + ", Rate=" + str(match_rate) + ", Failures=" + str(failed)
        log.append(summary)
        for item in self.status_matched:
            log.append(item)
        for item in self.status_failed:
            log.append(item)

        return log


