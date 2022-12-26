import pytest

from .solution import palindrome_index

# def test(test_case, solution):
#     assert hackerrank_main(test_case) == solution
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         s = input()

#         result = palindrome_index(s)

#         fptr.write(str(result) + '\n')

#     fptr.close()


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    t = int(input_lines.pop(0).strip())

    results = []
    for _ in range(t):
        input_str = input_lines.pop(0).rstrip()
        result = palindrome_index(input_str)
        results.append(result)

    return results


TEST_CASE_0 = """3
aaab
baa
aaa"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, [3, 0, -1]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
