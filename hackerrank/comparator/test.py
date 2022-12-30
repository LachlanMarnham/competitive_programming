from functools import cmp_to_key

import pytest

from .solution import Player


def hackerrank_main(test_case):
    input_lines = test_case.strip().splitlines()
    n = int(input_lines.pop(0).strip())
    data = []
    for _ in range(n):
        name, score = input_lines.pop(0).strip().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    results = []
    for i in data:
        results.append(repr(i))
    return "\n".join(results)


TEST_CASE_0 = """5
amy 100
david 100
heraldo 50
aakansha 75
aleksa 150"""

SOLUTION_0 = """aleksa 150
amy 100
david 100
aakansha 75
heraldo 50"""

TEST_CASE_6 = """3
smith 20
jones 15
jones 20"""

SOLUTION_6 = """jones 20
smith 20
jones 15"""

TEST_CASE_7 = """4
davis 15
davis 20
davis 10
edgehill 15"""

SOLUTION_7 = """davis 20
davis 15
edgehill 15
davis 10"""


@pytest.mark.parametrize(
    "test_case, solution",
    (
        (TEST_CASE_0, SOLUTION_0),
        (TEST_CASE_6, SOLUTION_6),
        (TEST_CASE_7, SOLUTION_7),
    ),
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
