from .solution import truck_tour


def hackerrank_main(test_case):
    input_lines = test_case.strip().splitlines()
    n = int(input_lines.pop(0).strip())

    petrol_pumps = []

    for _ in range(n):
        petrol_pumps.append(list(map(int, input_lines.pop(0).split())))

    return truck_tour(petrol_pumps)


TEST_CASE_0 = """2
10 3
3 4"""


def test():
    assert hackerrank_main(TEST_CASE_0) == 0
