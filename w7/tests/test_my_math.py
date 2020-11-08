from my_mathematics.simple_math import MyMath
import math
import pytest


@pytest.mark.parametrize('x', [0, 1, 2, 3, 4, 5, 0.01, 3e-7, 232, 213123, 392, 921])
def test_check_sine(x):
    assert math.sin(x) == MyMath.sin(x)


def test_check_pi():
    assert round(math.pi, 2) == MyMath.pi


@pytest.mark.parametrize('x', [0, 1, 2, 3, 4, 5, 0.01, 3e-7, 232, 213123, 392, 921])
def test_check_sqrt(x):
    assert math.sqrt(x) == MyMath.sqrt(x)


@pytest.mark.xfail
@pytest.mark.parametrize('x', [-1, -4, -5, -2])
def test_neg_sqrt(x):
    assert math.sqrt(x) == MyMath.sqrt(x)
