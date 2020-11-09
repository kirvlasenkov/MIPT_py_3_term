from scripts.ex_4 import get_cartesian_product
from itertools import product
import pytest


@pytest.mark.parametrize("lhs, rhs", [
    ([1, 2, 3, 4], ["a", "ca", "ac"]),
    ([1, 2, 3, 4], [])
])
def test_product(lhs, rhs):
    assert list(product(lhs, rhs)) == list(get_cartesian_product(lhs, rhs))
