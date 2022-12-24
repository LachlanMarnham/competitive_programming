import pytest

from .solution import fizz_buzz


def hackerrank_main(test_case):
    return fizz_buzz(test_case)


INPUT_0 = 15

OUTPUT_0 = """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz"""

INPUT_1 = 65

OUTPUT_1 = """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz"""

INPUT_2 = 12

OUTPUT_2 = """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz"""


@pytest.mark.parametrize('test_case, solution', [
    (INPUT_0, OUTPUT_0),
    (INPUT_1, OUTPUT_1),
    (INPUT_2, OUTPUT_2),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution.splitlines()
