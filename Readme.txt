Objective:
-   Have a tool that can on-board majority of the users' offline(often Pirated!) songs to legitimate streaming/cloud services
-   Start with support for Amazon Music, add other platforms later on. Browser support: Chrome
-   Project Prefs: Python 3.8.2, IDE: PyCharm, the venv should auto resolve most of the dependencies.

What to run/driver:
-   Run UserConfig.py to run the end to end scenario.
-   All of the selenium automation is in the Getter/Setter drivers, run them via TestDriver.py
    Ensure the version of the Chrome browser and the ChromeDrivers match, download the file/update as needed.
    Update user/pass for local testing *only*.
-   The Name/Dir handlers can be tested via TestNames.py


TODO
-   Ensure DirHandler can handle paths across both supported OS.
-   Add handling for the odd case ( FuzzyMatcher )
-   Ensure proper exception handling/logging.

STATUS

----13-05-2020 21:05:00
-   Implemented Logger, need to add appropriate logs where necessary.
-   Added UserConfig/Orchestrator modules for end-to-end execution.
-   Refactored files




----10-05-2020 05:05:00
-   Worked toward the usecase of porting a playlist from one service to another.
-   Drivers now split into Getters(playlist fetch) and Setters(Creating a playlist)
-   Refactored files


----03-05-2020 19:20:00
-   Added Driver for Spotify
-   Minor improvements to implementations.



----26-04-2020 00:44:00
-   Added the FuzzyMatcher Utility module.
-   Overall AmazonMusic driver's reliability increased
-   Improved DirHandler


----15-04-2020 22:50:00
-   Added Metadata handling which serves as the primary source of artist/title info.


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
