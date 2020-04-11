Objective:
-   Have a tool that can on-board majority of the users' offline(often Pirated!) songs to legitimate streaming/cloud services
-   Start with support for Amazon Music, add other platforms later on. Browser support: Chrome
-   Python 3.8.2

What to run/driver:
-   All of the selenium automation is in ChromeDriverAmazonMusic.py, run it via TestDriver.py
-   Ensure you set the appropriate path to the chromedriver depending on the OS, download the file/update as needed.
-   Update user/pass for local testing *only*

TODO
-   Refactor find_assets(), too big too messy already. Also, handle the case for no results at all
    At least the annoying exceptions are sorted ¯\_(ツ)_/¯
-   Improve filename modules.

STATUS

----12-04-2020 01:54:00
-   Selenium Crap fixed. Elements needed to be in view to be interactable...
-   TODO:Work on Filename handling, currently the modules are TOO STRICT, very specific to mp3fiber.com/other styles...
-   TODO:Incorporate youtube/IDM filename types along others


----11-04-2020
-   Stuck with a bit of Selenium : finding the elements off the dynamic contextMenu
    ( after finding the Tile, try adding the song to the playlist, can't seem to find "Add to playlist"...)