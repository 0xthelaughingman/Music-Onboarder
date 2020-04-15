import os


class DirHandler:
    path = ""
    file_list = []

    def __init__(self,  dir_path):
        self.path = dir_path

    def set_files(self):
        for file in os.listdir(self.path):
            if file.endswith(".mp3") or file.endswith(".mp4"):
                file = file.replace("_", " ")
                self.file_list.append(self.path + "\\" + file)

    def get_files(self):
        self.set_files()
        return self.file_list


if __name__ == "__main__":
    ob = DirHandler("path")
    print(ob.get_files())
