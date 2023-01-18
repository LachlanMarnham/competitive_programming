import pytest

from .solution import ceasar_cipher


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    _ = int(input_lines.pop(0).strip())
    s = input_lines.pop(0).strip()
    k = int(input_lines.pop(0).strip())
    return ceasar_cipher(s, k)


TEST_CASE_5 = """11
middle-Outz
2"""

TEST_CASE_11 = """38
Always-Look-on-the-Bright-Side-of-Life
5"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_5, "okffng-Qwvb"),
        (TEST_CASE_11, "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
