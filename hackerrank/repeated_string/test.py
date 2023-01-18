import pytest

from .solution import repeated_string


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()

    sub_string = input_lines.pop(0)

    n = int(input_lines.pop(0).strip())

    return repeated_string(sub_string, n)


TEST_CASE_0 = """aba
10"""

TEST_CASE_1 = """a
1000000000000"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, 7),
        (TEST_CASE_1, 1000000000000),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
