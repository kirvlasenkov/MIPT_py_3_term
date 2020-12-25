from scripts.ex_3 import my_zip, my_map, my_enumerate
import pytest


@pytest.mark.parametrize("lhs, rhs", [([1, 2, 3], [0, 32, 4]), ([1], range(10)), ([], [])])
def test_zip(lhs, rhs):
    assert list(my_zip(lhs, rhs)) == list(zip(lhs, rhs))


@pytest.mark.parametrize("arg", [(1, 2, 3, 4), [12, 23, 23, 23, 23], []])
def test_enumerate(arg):
    for elem in zip(my_enumerate(arg), enumerate(arg)):
        assert elem[0] == elem[1]


@pytest.mark.parametrize("func, arg", [(lambda x: x ** 2, [1, 2, 3, 4])])
def test_map(func, arg):
    for elem in zip(my_map(func, arg), map(func, arg)):
        assert elem[0] == elem[1]
