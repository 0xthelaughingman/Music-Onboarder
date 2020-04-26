from AmazonMusicDriver import AmazonMusicDriver
from SpotifyDriver import SpotifyDriver
from DirHandler import DirHandler
from NameHandler import NameHandler

# file_names = DirHandler("path").get_files()
# asset_list = NameHandler(file_names).get_pairs()
# Update details as needed
# print(asset_list)
# ob = ChromeDriver.ChromeDriverAmazonMusic(True, "email", "pass", "Testing", asset_list)
ob = AmazonMusicDriver(True, "email", "pass", "Testing")
ob = SpotifyDriver(True, "email", "pass", "Testing")

results = ob.get_status()
for i in results:
    print(i)
