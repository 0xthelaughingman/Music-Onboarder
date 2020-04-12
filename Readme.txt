Objective:
-   Have a tool that can on-board majority of the users' offline(often Pirated!) songs to legitimate streaming/cloud services
-   Start with support for Amazon Music, add other platforms later on. Browser support: Chrome
-   Project Prefs: Python 3.8.2, IDE: PyCharm, the venv should auto resolve most of the dependencies.

What to run/driver:
-   All of the selenium automation is in ChromeDriverAmazonMusic.py, run it via TestDriver.py
-   Ensure the version of the Chrome browser and the ChromeDrivers match, download the file/update as needed.
-   Update user/pass for local testing *only*.


TODO
-   Refactor find_assets(), too big too messy already. At least the annoying exceptions are out of the way. ¯\_(ツ)_/¯
-   Improve filename modules.
-   Work on a better/less strict matching/comparison approach, incase the service doesn't yield the exact asset.

STATUS

----12-04-2020 21:50:00
-   Handled the case for "No Results" for an asset.
-   Swapped out sleeps for implicit wait.
-   TODO: Improve File/Name modules.


----12-04-2020 01:54:00
-   Selenium Crap fixed. Elements needed to be in view to be interactable...
-   TODO:Work on Filename handling, currently the modules are TOO STRICT, very specific to mp3fiber.com/other styles...
-   TODO:Incorporate youtube/IDM filename types along others.


----11-04-2020
-   Stuck with a bit of Selenium : finding the elements off the dynamic contextMenu.
    ( after finding the Tile, try adding the song to the playlist, can't seem to find "Add to playlist"...).