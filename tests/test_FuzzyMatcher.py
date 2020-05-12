from source.FuzzyMatcher import FuzzyMatcher


def test_get_match_factor():
    duo_case_1()
    duo_case_2()
    duo_case_3()
    duo_case_4()
    duo_case_N()


# Tests, ensure these are maintained while adding further combinations/cases.
def duo_case_1():
    assert FuzzyMatcher.get_match_factor(3, 'tyzo bloom', 'ukiyo', 'tyzo bloom', 'ukiyo') == 1.0
    assert FuzzyMatcher.get_match_factor(3, 'ukiyo', 'tyzo bloom', 'tyzo bloom', 'ukiyo') == 1.0


def duo_case_2():
    assert FuzzyMatcher.get_match_factor(3, 'tyzo bloom', 'ukiyo', 'tyzo blo', 'ukiyo') == 0.9
    assert FuzzyMatcher.get_match_factor(3, 'tyzo blo', 'ukiyo', 'tyzo bloom', 'ukiyo') == 0.9

    assert FuzzyMatcher.get_match_factor(3, 'tyzo bloom', 'uki', 'tyzo bloom', 'ukiyo') == 0.9
    assert FuzzyMatcher.get_match_factor(3, 'tyzo bloom', 'ukiyo', 'tyzo bloom', 'uk') == 0.9


def duo_case_3():
    assert FuzzyMatcher.get_match_factor(3, 'tyzo blo', 'uki', 'tyzo bloom', 'ukiyo') == 0.7
    assert FuzzyMatcher.get_match_factor(3, 'tyzo bloom', 'ukiyo', 'tyzo blo', 'uk') == 0.7


def duo_case_4():
    assert FuzzyMatcher.get_match_factor(3, 'tyzo bloom', 'ukiyo', 'tyzo blo', 'uz') == 0.4
    assert FuzzyMatcher.get_match_factor(3, 'tz bloom', 'ukiyo', 'tyzo blo', 'ukiyo') == 0.4


def duo_case_N():
    assert FuzzyMatcher.get_match_factor(3, 'tzo blm', 'uyo', 'tyzo blo', 'uz') == 0.0
