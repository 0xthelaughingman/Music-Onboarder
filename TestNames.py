from source.DirHandler import DirHandler
from source.NameHandler import NameHandler


file_names = DirHandler("path").get_files()
asset_list = NameHandler(file_names).get_pairs()

for i in range(0, len(asset_list)):
    print("%06d - %s   ......   %s" %(i, asset_list[i], file_names[i]))
