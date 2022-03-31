import pytest

from .solution import left_join


def checkio_main(phrases, solution):
    assert left_join(phrases) == solution


@pytest.mark.parametrize('phrases, solution', [
    (('left', 'right', 'left', 'stop'), 'left,left,left,stop'),
    (('bright aright', 'ok'), 'bleft aleft,ok'),
    (('brightness wright',), 'bleftness wleft'),
    (('enough', 'jokes'), 'enough,jokes'),
])
def test(phrases, solution):
    checkio_main(phrases, solution)
