import pytest

from .solution import sock_merchant


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()

    _ = int(input_lines.pop(0).strip())

    arr = list(map(int, input_lines.pop(0).rstrip().split()))

    return sock_merchant(arr)


TEST_CASE_0 = """9
10 20 20 10 10 30 50 10 20"""

TEST_CASE_8 = """10
1 1 3 1 2 1 3 3 3 3"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, 3),
        (TEST_CASE_8, 4),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
