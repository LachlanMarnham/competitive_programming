import pytest

from .solution import is_all_upper


def checkio_main(text, solution):
    assert is_all_upper(text) == solution


@pytest.mark.parametrize('text, solution', [
    ('ALL UPPER', True),
    ('all lower', False),
    ('mixed UPPER and lower', False),
    ('', True),
    ('     ', True),
    ('444', True),
    ('55 55 5', True),
])
def test(text, solution):
    checkio_main(text, solution)
