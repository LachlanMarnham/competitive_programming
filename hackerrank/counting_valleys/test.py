import pytest

from .solution import counting_valleys


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    _ = int(input_lines.pop(0).strip())
    path = input_lines.pop(0)
    return counting_valleys(path)


TEST_CASE_0 = """8
UDDDUDUU"""

TEST_CASE_1 = """12
DDUUDDUDUUUD"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, 1),
        (TEST_CASE_1, 2),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
