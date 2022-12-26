import pytest

from .solution import grid_challenge


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    t = int(input_lines.pop(0).strip())
    results = []
    for _ in range(t):
        n = int(input_lines.pop(0).strip())
        grid = []
        for _ in range(n):
            grid_item = input_lines.pop(0)
            grid.append(grid_item)

        result = grid_challenge(grid)

        results.append(result)
    return results


TEST_CASE_0 = """1
5
eabcd
fghij
olkmn
trpqs
xywuv"""

TEST_CASE_12 = """3
3
abc
lmp
qrt
3
mpxz
abcd
wlmf
4
abc
hjk
mpq
rtv"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, ["YES"]),
        (TEST_CASE_12, ["YES", "NO", "YES"]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
