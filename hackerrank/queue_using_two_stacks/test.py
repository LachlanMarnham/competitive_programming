from .solution import queue_using_two_stacks


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    _ = int(input_lines.pop(0).strip())
    return queue_using_two_stacks(input_lines)


TEST_CASE_0 = """10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2"""


def test():
    assert hackerrank_main(TEST_CASE_0) == [14, 14]
