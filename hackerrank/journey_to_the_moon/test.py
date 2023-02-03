import pytest


from .solution import journey_to_moon


@pytest.mark.parametrize('n, astronauts, output',(
    (5, [[0, 1], [2, 3], [0, 4]], 6),
    (4, [[0, 2]], 5),
))
def test(n, astronauts, output):
    assert journey_to_moon(n, astronauts) == output

