import pytest
from main import get_degree
"""distance test.

    Args:
        rdu: float - radius
        time: float - time
        vel: float - velocity

    Returns:
        float - degree of rotation
    """
arr = (
        ((2.0, 10.0, 1.0), 1432.39),
        ((2, 10, 1), 1432.39),
)


@pytest.mark.parametrize('zna, otvet', arr)
def test_main(zna, otvet):
    assert get_degree(*zna) == otvet
