from my_mathematics.simple_math import MyComplexMath
import pytest
import cmath
import numpy as np


@pytest.mark.parametrize('x', [1 + 3j, 2 - 7j, 0, -2, 3 + 0j, 1j, 8])
def test_check_sine(x):
    assert np.sin(x).real == MyComplexMath.sin(x).real
    assert np.sin(x).imag == MyComplexMath.sin(x).imag


def test_check_pi():
    assert round(cmath.pi, 2) == MyComplexMath.pi


@pytest.mark.parametrize('x', [-1, -2, -3, -4, -5, -4, -3e-7, -232, -213123, -392, -921])
def test_check_sqrt(x):
    assert cmath.sqrt(x).real == MyComplexMath.sqrt(x)[0] and \
           cmath.sqrt(x).imag == MyComplexMath.sqrt(x)[1]
