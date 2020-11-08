from my_mathematics.linear_algebra import MyVector
import pytest
import numpy as np


@pytest.mark.parametrize('lhs, rhs', [(MyVector(3, 2, 3, 4), MyVector(3, 0, 6, 4)),
                                      (MyVector(2, 3, 4), MyVector(2, 1, 0)),
                                      (MyVector(2, 3, 4), MyVector(2, 1, 0)),
                                      (MyVector(1, 9), MyVector(1, 2)),
                                      (MyVector(5, 2, 1, 3, 4, 5), MyVector(5, 4, 10, 6, 3, 4))
                                      ]
                         )
def test_vector_sum(lhs, rhs):
    np_lhs = lhs.args_as_np
    np_rhs = rhs.args_as_np

    assert (lhs + rhs).args_as_np.all() == (np_lhs + np_rhs).all()


@pytest.mark.parametrize('lhs, rhs', [(MyVector(3, 2, 3, 4), MyVector(3, 0, 6, 4)),
                                      (MyVector(2, 3, 4), MyVector(2, 1, 0)),
                                      (MyVector(2, 3, 4), MyVector(2, 1, 0)),
                                      (MyVector(1, 9), MyVector(1, 2)),
                                      (MyVector(5, 2, 1, 3, 4, 5), MyVector(5, 4, 10, 6, 3, 4))
                                      ]
                         )
def test_vector_sub(lhs, rhs):
    np_lhs = lhs.args_as_np
    np_rhs = rhs.args_as_np

    assert (lhs - rhs).args_as_np.all() == (np_lhs - np_rhs).all()


@pytest.mark.parametrize('lhs, rhs', [(MyVector(3, 2, 3, 4), MyVector(3, 0, 6, 4)),
                                      (MyVector(2, 3, 4), MyVector(2, 1, 0)),
                                      (MyVector(2, 3, 4), MyVector(2, 1, 0)),
                                      (MyVector(1, 9), MyVector(1, 2)),
                                      (MyVector(5, 2, 1, 3, 4, 5), MyVector(5, 4, 10, 6, 3, 4))
                                      ]
                         )
def test_vector_dot_product(lhs, rhs):
    np_lhs = lhs.args_as_np
    np_rhs = rhs.args_as_np
    np_dot = np_lhs.dot(np_rhs)

    assert lhs * rhs == np_dot


@pytest.mark.parametrize('vector', [MyVector(1, 0), MyVector(2, 3, 1), MyVector(3, 4, 5, 9),
                                 MyVector(4, 1, 3, 6, 4), MyVector(5, 9, 8, 5, 3, 9), MyVector(6, 5, 6, 8, 9, 0, 8)
                                 ]
                         )
def test_vector_norm(vector):
    np_vector = vector.args_as_np

    assert np.linalg.norm(np_vector) == vector.vector_norm()
