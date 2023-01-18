import pytest

from .solution import is_balanced


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    t = int(input_lines.pop(0).strip())
    results = []
    for _ in range(t):
        s = input_lines.pop(0)
        result = is_balanced(s)
        results.append(result)
    return results


TEST_CASE_18 = """3
{[()]}
{[(])}
{{[[(())]]}}"""

TEST_CASE_19 = """2
{{([])}}
{{)[](}}"""

TEST_CASE_20 = """3
{(([])[])[]}
{(([])[])[]]}
{(([])[])[]}[]"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_18, ["YES", "NO", "YES"]),
        (TEST_CASE_19, ["YES", "NO"]),
        (TEST_CASE_20, ["YES", "NO", "YES"]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
