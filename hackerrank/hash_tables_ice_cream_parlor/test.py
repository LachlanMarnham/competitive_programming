import pytest

from .solution import what_flavours


def hackerrank_main(test_case):
    outputs = []

    input_lines = test_case.splitlines()
    t = int(input_lines.pop(0).strip())
    for _ in range(t):
        money = int(input_lines.pop(0).strip())

        _ = int(input_lines.pop(0).strip())

        cost = list(map(int, input_lines.pop(0).rstrip().split()))
        output = what_flavours(cost, money)
        outputs.append(output)

    return outputs


TEST_CASE_14 = """2
4
5
1 4 5 3 2
4
4
2 2 4 3"""

TEST_CASE_15 = """1
5
5
1 2 3 5 6"""

TEST_CASE_16 = """2
8
5
4 3 2 5 7
12
5
7 2 5 4 11"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_14, ["1 4", "1 2"]),
        (TEST_CASE_15, ["2 3"]),
        (TEST_CASE_16, ["2 4", "1 3"]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
