import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "input, output",
    (
        ("25525511135", ["255.255.11.135", "255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
        ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
    ),
)
def test(input, output):
    solver = Solution()
    result = set(solver.restore_ip_addresses(input))
    expected_result = set(output)
    assert result == expected_result
