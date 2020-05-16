"""
Utility Module to handle matching of the service asset to the file/playlist asset.
Should return a mathematical probability/factor of how good the match is.
Preferably the range [0,1], 1 being a perfect match.
Testfile: test_FuzzyMatcher.py (pytest)

"""


class FuzzyMatcher(object):
    # Thoroughly test your changes before tinkering with this method!
    @staticmethod
    def get_match_factor(file_type, file_artist, file_title, serv_artist, serv_title):
        if file_type < 2 or file_artist == file_title:
            return FuzzyMatcher.compare_single(file_artist, serv_artist, serv_title)
        else:
            return FuzzyMatcher.compare_duos(file_artist, file_title, serv_artist, serv_title)

    @staticmethod
    def compare_single(text, serv_artist, serv_title):
        return 0.2

    @staticmethod
    def compare_duos(file_artist, file_title, serv_artist, serv_title):
        # Case 1 : The artist/title info is an exact match, just unsure of the order.
        if (file_title == serv_title or file_title == serv_artist) and \
                (file_artist == serv_artist or file_artist == serv_title):
            return 1.0

        # Case 2 : One of them is an exact match, the other a substring
        if file_title == serv_title or file_title == serv_artist:
            if FuzzyMatcher.check_substrings(file_artist, serv_artist) or \
                    FuzzyMatcher.check_substrings(file_artist, serv_title):
                return 0.9

        if file_artist == serv_title or file_artist == serv_artist:
            if FuzzyMatcher.check_substrings(file_title, serv_artist) or \
                    FuzzyMatcher.check_substrings(file_title, serv_title):
                return 0.9

        # Case 3 : Neither is an exact match but each is at least present as a substring.
        if (FuzzyMatcher.check_substrings(file_artist, serv_artist) or
            FuzzyMatcher.check_substrings(file_artist, serv_title)) and \
                (FuzzyMatcher.check_substrings(file_title, serv_artist) or
                 FuzzyMatcher.check_substrings(file_title, serv_title)):
            return 0.7

        # Worst Possible Case : At least one of them is present as a substring in either the artist/title..
        if (FuzzyMatcher.check_substrings(file_artist, serv_artist) or
            FuzzyMatcher.check_substrings(file_artist, serv_title)) or \
                (FuzzyMatcher.check_substrings(file_title, serv_artist) or
                 FuzzyMatcher.check_substrings(file_title, serv_title)):
            return 0.4

        # Nothing is a possible match.
        return 0.0

    # Check both ways!
    @staticmethod
    def check_substrings(str1: str, str2: str):
        if str1.find(str2) >= 0 or str2.find(str1) >= 0:
            return True
        return False



