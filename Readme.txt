Objective:
-   Have a tool that can on-board majority of the users' offline(often Pirated!) songs to legitimate streaming/cloud services
-   Start with support for Amazon Music, add other platforms later on. Browser support: Chrome
-   Python 3.8.2

What to run/driver:
----PRIMARY:
-   All of the selenium automation is in ChromeDriverAmazonMusic.py
-   Ensure you set the appropriate path to the chromedriver depending on the OS, download the file/update as needed.
-   Update user/pass for local testing *only*
----OTHERS:
-   Low priority modules, first comes the selenium automation.
-   There are different handler modules on how to deal with the files/ file names.
-   Will also need a fuzzy/approximation module to match the assets with those available on the services.

STATUS
----11-04-2020
-   Stuck with a bit of Selenium : finding the elements off the dynamic contextMenu
    ( after finding the Tile, try adding the song to the playlist, can't seem to find "Add to playlist"...)