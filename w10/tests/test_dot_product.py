import pytest

from ..hw_scripts.pool_dot import dot_product
from my_mathematics.linear_algebra import MyVector


@pytest.mark.parametrize('lhs, rhs', [(MyVector(3, 2, 3, 4), MyVector(3, 0, 6, 4)),
                                      (MyVector(2, 3, 4), MyVector(2, 1, 0)),
                                      (MyVector(2, 3, 4), MyVector(2, 1, 0)),
                                      (MyVector(1, 9), MyVector(1, 2)),
                                      (MyVector(5, 2, 1, 3, 4, 5), MyVector(5, 4, 10, 6, 3, 4))
                                      ]
                         )
def test_dot_product_on_multithreading(lhs, rhs):
    assert round(dot_product(lhs, rhs, 1)[0], 5) == \
           round(lhs.args_as_np.dot(rhs.args_as_np), 5)

    assert round(dot_product(lhs, rhs, 2)[0], 5) == \
           round(lhs.args_as_np.dot(rhs.args_as_np), 5)

    assert round(dot_product(lhs, rhs, 4)[0], 5) == \
           round(lhs.args_as_np.dot(rhs.args_as_np), 5)


@pytest.mark.parametrize('lhs, rhs', [(MyVector(3, 2, 3, 4), MyVector(3, 0, 6, 4)),
                                      (MyVector(2, 3, 4), MyVector(2, 1, 0)),
                                      (MyVector(2, 3, 4), MyVector(2, 1, 0)),
                                      (MyVector(1, 9), MyVector(1, 2)),
                                      (MyVector(5, 2, 1, 3, 4, 5), MyVector(5, 4, 10, 6, 3, 4))
                                      ]
                         )
def test_dot_product_on_multiprocessing(lhs, rhs):
    assert round(dot_product(lhs, rhs, 1)[0], 5) == \
           round(lhs.args_as_np.dot(rhs.args_as_np), 5)

    assert round(dot_product(lhs, rhs, 2)[0], 5) == \
           round(lhs.args_as_np.dot(rhs.args_as_np), 5)

    assert round(dot_product(lhs, rhs, 4)[0], 5) == \
           round(lhs.args_as_np.dot(rhs.args_as_np), 5)
