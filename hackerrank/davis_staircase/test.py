import pytest

from .solution import step_perms


def hackerrank_main(test_case):
    input_lines = test_case.strip().splitlines()

    s = int(input_lines.pop(0).strip())
    results = []
    for _ in range(s):
        n = int(input_lines.pop(0).strip())
        result = step_perms(n)
        results.append(result)

    return results


TEST_CASE_0 = """3
1
3
7"""

TEST_CASE_9 = """2
5
8"""

TEST_CASE_10 = """3
15
20
27"""


@pytest.mark.parametrize(
    "test_case, solution",
    (
        (TEST_CASE_0, [1, 4, 44]),
        (TEST_CASE_9, [13, 81]),
        (TEST_CASE_10, [5768, 121415, 8646064]),
    ),
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
