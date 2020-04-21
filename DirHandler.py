import os


class DirHandler(object):
    def __init__(self, path):
        self.__midea_files = []
        if (self.__is_valid_path(path)):
            self.__search_midea_files(path)

    def __search_midea_files(self, path):
        if(self.__is_midea(path)):
            self.__midea_files.append(path)
            return

        if(not self.__is_dir(path)):
            return
        
        dir_items = os.listdir(path)
        for item in dir_items:
            self.__search_midea_files("%s/%s" %(path,item))

    def __is_dir(self, path):
        return os.path.isdir(path)
    
    def __is_midea(self, path):
        return path.endswith("mp3") or path.endswith(".mp4")
    
    def __is_valid_path(self, path):
        return os.path.exists(path)

    def get_files(self):
        return self.__midea_files


if __name__ == "__main__":
    midea_files = DirHandler("path").get_files()
    counter = 0;
    for file in midea_files:
        counter += 1
        print("%06d - %s" %(counter, file))
