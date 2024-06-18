import math

import pytest

from pyalgo_tools import circle_overlap_area, dhondt


def test_dhondt():
    actual = dhondt(100, [45, 12, 34])
    assert (actual == [50, 13, 37]).all()


@pytest.mark.parametrize(
    "memo, x1, y1, r1, x2, y2, r2, expected",
    [
        ("重ならない", 0, 2, 1, 2, 0, 1, 0),
        ("含まれる", 0, 2, 1, 0, 1, 2, 3.1416),
        ("重なる", 0, 2, 1, 0, 0, 2, 1.403),
    ],
)
def test_circle_overlap_area(memo, x1, y1, r1, x2, y2, r2, expected):
    actual = circle_overlap_area(x1, y1, r1, x2, y2, r2)
    assert math.isclose(actual, expected, abs_tol=0.001), memo
