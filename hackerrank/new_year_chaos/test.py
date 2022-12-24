import pytest

from .solution import minimum_bribes


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    t = int(input_lines.pop(0).strip())

    results = []
    for _ in range(t):
        _ = int(input_lines.pop(0).strip())
        q = list(map(int, input_lines.pop(0).rstrip().split()))
        result = minimum_bribes(q)
        results.append(result)

    return results


TEST_CASE_0 = """2
5
2 1 5 3 4
5
2 5 1 3 4"""

TEST_CASE_1 = """2
8
5 1 2 3 7 8 6 4
8
1 2 5 3 7 8 6 4"""

TEST_CASE_2 = """1
8
1 2 5 3 4 7 8 6"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, [3, "Too chaotic"]),
        (TEST_CASE_1, ["Too chaotic", 7]),
        (TEST_CASE_2, [4]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
