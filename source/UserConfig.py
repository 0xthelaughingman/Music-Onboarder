"""
Module to oversee the end to end flow of the conversion of the music assets as decided
by the User.
"""
from source.supported_configs import *
from source.Orchestrator import Orchestrator

1
class UserConfig:

    def __init__(self):
        print("Pick conversion source (integer):\n")
        for i in range(0, len(getters_list)):
            print(str(i) + " : " + getters_list[i])

        source_opt = int(input())
        if source_opt < 0 or source_opt >= len(getters_list):
            print("Incorrect Option.")
            quit()

        if source_opt > 0:
            setters_list.remove(getters_list[source_opt])

        print("Enter playlist url/path to directory\n")
        playlist_src = input()

        print("Pick conversion destination (integer):\n")
        for i in range(0, len(setters_list)):
            print(str(i) + " : " + setters_list[i])

        dest_opt = int(input())
        if dest_opt < 0 or dest_opt >= len(setters_list):
            print("Incorrect Option.")
            quit()

        src_type = getters_list[source_opt]
        dest_type = setters_list[dest_opt]

        Orchestrator(src_type, playlist_src, dest_type)


if __name__ == "__main__":
    ob = UserConfig()
