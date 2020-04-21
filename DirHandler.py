import os


class DirHandler(object):
    def __init__(self, path):
        self.__media_files = []
        if (self.__is_valid_path(path)):
            self.__search_media_files(path)

    def __search_media_files(self, path):
        if(self.__is_media(path)):
            self.__media_files.append(path)
            return

        if(not self.__is_dir(path)):
            return
        
        dir_items = os.listdir(path)
        for item in dir_items:
            self.__search_media_files("%s/%s" %(path,item))

    def __is_dir(self, path):
        return os.path.isdir(path)
    
    def __is_media(self, path):
        return path.endswith("py") or path.endswith(".mp4")
    
    def __is_valid_path(self, path):
        return os.path.exists(path)

    def get_files(self):
        return self.__media_files


if __name__ == "__main__":
    media_files = DirHandler("path").get_files()
    counter = 0;
    for file in media_files:
        counter += 1
        print("%06d - %s" %(counter, file))
