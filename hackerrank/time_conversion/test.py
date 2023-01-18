from .solution import time_conversion


def hackerrank_main(test_case):
    return time_conversion(test_case)


TEST_CASE_0 = "07:05:45PM"


def test():
    assert hackerrank_main(TEST_CASE_0) == "19:05:45"
