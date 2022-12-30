import pytest

from .solution import SinglyLinkedList, merge_lists


def get_result(node):
    results = []
    while node:
        results.append(node.data)
        node = node.next
    return results


def hackerrank_main(test_case):
    input_lines = test_case.strip().splitlines()
    tests = int(input_lines.pop(0).strip())
    results = []
    for _ in range(tests):
        list_1_length = int(input_lines.pop(0).strip())
        list_1 = SinglyLinkedList()
        for _ in range(list_1_length):
            datum = int(input_lines.pop(0).strip())
            list_1.insert_node(datum)

        list_2_length = int(input_lines.pop(0).strip())
        list_2 = SinglyLinkedList()
        for _ in range(list_2_length):
            datum = int(input_lines.pop(0).strip())
            list_2.insert_node(datum)

        list_3_head = merge_lists(list_1.head, list_2.head)
        result = get_result(list_3_head)
        results.append(result)
    return results


TEST_CASE_0 = """1
3
1
2
3
2
3
4"""

TEST_CASE_1 = """1
3
4
5
6
3
1
2
10"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, [[1, 2, 3, 3, 4]]),
        (TEST_CASE_1, [[1, 2, 4, 5, 6, 10]]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
