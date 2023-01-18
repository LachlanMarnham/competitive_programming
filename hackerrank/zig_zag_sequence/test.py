import pytest

from .solution import find_zig_zag_sequence


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    _ = int(input_lines.pop(0).strip())
    n = int(input_lines.pop(0).strip())
    arr = list(map(int, input_lines.pop(0).strip().split()))
    return find_zig_zag_sequence(arr, n)


TEST_CASE_0 = """1
7
1 2 3 4 5 6 7"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, [1, 2, 3, 7, 6, 5, 4]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
