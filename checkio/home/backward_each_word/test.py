import pytest

from .solution import backward_string_by_word


def checkio_main(text, solution):
    assert backward_string_by_word(text) == solution


@pytest.mark.parametrize('text, solution', [
    ('', ''),
    ('world', 'dlrow'),
    ('hello world', 'olleh dlrow'),
    ('hello   world', 'olleh   dlrow'),
    ('welcome to a game', 'emoclew ot a emag'),
])
def test(text, solution):
    checkio_main(text, solution)
