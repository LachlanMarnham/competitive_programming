import pytest

from .solution import nearest_value


def checkio_main(values, target, solution):
    assert nearest_value(values, target) == solution


@pytest.mark.parametrize('values, target, solution', [
    ({0, -2}, -1, -2),
    ({4, 7, 10, 11, 12, 17}, 9, 10),
    ({4, 7, 10, 11, 12, 17}, 8, 7),
    ({4, 8, 10, 11, 12, 17}, 9, 8),
    ({4, 9, 10, 11, 12, 17}, 9, 9),
    ({4, 7, 10, 11, 12, 17}, 0, 4),
    ({4, 7, 10, 11, 12, 17}, 100, 17),
    ({5, 10, 8, 12, 89, 100}, 7, 8),
    ({5}, 5, 5),
    ({5}, 7, 5),
])
def test(values, target, solution):
    checkio_main(values, target, solution)
