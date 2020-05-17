"""
Base class for all supported services' Setters.
Important Notes:
It expects an test_mode, asset_list(list of assets to be added in the playlist) to be a mandatory input
The drivers are currently designed to be able to run as standalone modules to assist in testing.
sub class init prototype:(self, test_mode=False,  asset_list=list, email=None, password=None, playlist=None)

As such, the sub class constructors are expected to allow the following legal usage/param combinations:

-(self, test_mode=True, asset_list=list, email, password) -> Testing scenario, where the login is automated.

-(self, test_mode=False, asset_list=list, None, None, playlist_name) -> ETE case,
as is expected to be run from the app once the prerequisites are already collected in a separate module

"""

import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
import os
import time
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from urllib3.connectionpool import log as urllibLogger
urllibLogger.setLevel(logging.WARNING)
LOGGER.setLevel(logging.WARNING)


class DriverSetterBase:
    driver = None
    playlist_name = None
    asset_list = None
    status_matched = None
    status_failed = None
    exec_time = None
    logger = None

    def __init__(self):
        # Dynamic Path computation, handling execution from anywhere
        self.exec_time = time.time()
        self.logger = logging.getLogger()
        cur_path = os.getcwd()
        path_groups = cur_path.split("Music-Onboarder")
        dyn_path = cur_path
        rel_path = ""
        if path_groups[1] != '':
            counter = path_groups[1].count("\\")
            for i in range(0, counter):
                rel_path = rel_path + "../"
            dyn_path = rel_path

        # Only supporting win/Mac OS X
        if sys.platform == "win32":
            self.driver = webdriver.Chrome(dyn_path + '/webdriver/chromedriver.exe')
        else:
            self.driver = webdriver.Chrome(dyn_path + '/webdriver/chromedriver_mac64')
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

    def log_status(self):
        matched = len(self.status_matched)
        failed = len(self.status_failed)
        total = matched + failed
        match_rate = round(matched/total * 100, 2)

        total = len(self.asset_list)
        self.logger.critical("-"*40)
        self.logger.critical("SetterName:" + self.__class__.__name__)
        self.logger.critical(str("Total=%d, Matches=%d, Rate=%.2f, Failures=%d" % (total, matched, match_rate, failed)))

        for item in self.status_matched:
            self.logger.critical(item)
        for item in self.status_failed:
            self.logger.critical(item)

        self.logger.critical(str("Execution time=%.2f" % self.exec_time))
