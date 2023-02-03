from .solution import SummaryRanges


def test():
    tester = SummaryRanges()
    operations = [
        "add_num",
        "get_intervals",
        "add_num",
        "get_intervals",
        "add_num",
        "get_intervals",
        "add_num",
        "get_intervals",
        "add_num",
        "get_intervals",
    ]
    inputs = [[1], [], [3], [], [7], [], [2], [], [6], []]
    results = [
        None,
        [[1, 1]],
        None,
        [[1, 1], [3, 3]],
        None,
        [[1, 1], [3, 3], [7, 7]],
        None,
        [[1, 3], [7, 7]],
        None,
        [[1, 3], [6, 7]],
    ]
    for idx, operation in enumerate(operations):
        if operation == "add_num":
            tester.add_num(inputs[idx][0])
        elif operation == "get_intervals":
            assert tester.get_intervals() == results[idx]
