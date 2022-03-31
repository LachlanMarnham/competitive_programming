import pytest

from .solution import determine_order


def checkio_main(data, solution):
    assert determine_order(data) == solution


@pytest.mark.parametrize('data, solution', [
    (['a', 'b', 'c'], 'abc'),
    (['acb', 'bd', 'zwa'], 'zwacbd'),
    (['klm', 'kadl', 'lsm'], 'kadlsm'),
    (['aazzss'], 'azs'),
    (['dfg', 'frt', 'tyg'], 'dfrtyg'),
])
def test(data, solution):
    checkio_main(data, solution)
