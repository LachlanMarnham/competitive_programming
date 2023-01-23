import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "input, output",
    (
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
    ),
)
def test(input, output):
    solver = Solution()
    result = solver.partition(input)
    # Just to make it order agnostic
    result = {tuple(val) for val in result}
    expected_result = {tuple(val) for val in output}
    assert result == expected_result
