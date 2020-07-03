# Music Onboarder
Objective:
* Have a tool that can on-board majority of the users' offline(often Pirated!) songs to legitimate streaming/cloud services
* Start with support for Amazon Music, Spotify add other platforms later on. Browser support: Chrome
* Project Prefs: Python 3.8.2, IDE: PyCharm, the venv should auto resolve most of the dependencies.

# What to run/driver:
* Run UserConfig.py to run the end to end scenario.
* All of the selenium automation is in the Getter/Setter drivers, run them via TestDriver.py
  Ensure the version of the Chrome browser and the ChromeDrivers match, download the file/update as needed.
  Update user/pass for local testing *only*.
* The Name/Dir handlers can be tested via TestNames.py

# Known Issues
* ChromeDriver versions need to be updated as the browser updates.
* Spotify UI/layout changes disrupt Selenium flow now and then.


# TODOs
1. Ensure DirHandler can handle paths across both supported OS.
2. Add handling for the odd case ( FuzzyMatcher )
3. Ensure proper exception handling/logging.


