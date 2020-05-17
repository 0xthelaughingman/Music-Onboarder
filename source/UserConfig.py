"""
Module to oversee the end to end flow of the conversion of the music assets as decided
by the User.

"""

from source.supported_configs import *
from source.Orchestrator import Orchestrator


class UserConfig:

    def __init__(self):
        print("Pick conversion source (integer):\n")
        for i in range(0, len(getters_list)):
            print(str(i) + " : " + getters_list[i])

        while True:
            source_opt = int(input())
            if self.check_bounds(source_opt, getters_list) is True:
                break
            print("Incorrect Option. Retry")

        if source_opt > 0:
            setters_list.remove(getters_list[source_opt])

        print("Enter playlist url/path to directory\n")
        playlist_src = input()

        print("Pick conversion destination (integer):\n")
        for i in range(0, len(setters_list)):
            print(str(i) + " : " + setters_list[i])

        while True:
            dest_opt = int(input())
            if self.check_bounds(dest_opt, setters_list) is True:
                break
            print("Incorrect Option. Retry")

        src_type = getters_list[source_opt]
        dest_type = setters_list[dest_opt]

        Orchestrator(src_type, playlist_src, dest_type)

    def check_bounds(self, choice: int, choices: list):
        if choice < 0 or choice >= len(choices):
            return False
        return True


if __name__ == "__main__":
    ob = UserConfig()
