import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "input, num_rows, output",
    (
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
    ),
)
def test(input, num_rows, output):
    tester = Solution()
    assert tester.convert(input, num_rows) == output
