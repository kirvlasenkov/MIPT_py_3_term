from typing import Union
import numpy as np


class MyVector:
    """
    Simple class for the vector calculus
    on the finite Euclid space.
    """

    __slots__ = ("__dimension", "__args")  # needed for better memory allocation, as it's

    # locked creating brand new attributes.

    def __init__(self, dimension, *args: Union[int, float]):
        """
        Standard constructor.
        :param dimension: dimension of space
        :param args: coordinates of the vector
        """
        assert dimension >= 0
        assert len(args) == dimension, "You are trying to make me fool;" \
                                       " please, enter the vector from {}-dimensional" \
                                       " space".format(dimension)

        if dimension == 0:
            if list(args) == [0 for _ in range(dimension)]:
                self.__args = np.array(args)
            else:
                raise ValueError("vector from 0-dimensional space must be zero-vector")
        self.__dimension: int = dimension
        self.__args: np.array[Union[int, float]] = np.array(args)

    def __str__(self) -> str:
        string = '(' + ", ".join(map(str, self.__args)) + ')'
        return string

    def __neg__(self):
        self.__args = np.array(list(map(lambda x: -x, self.__args)))
        return self

    def __repr__(self) -> str:
        string = 'MyVector(' + ', '.join(map(str, self.__args)) + ')'
        return string

    def __mul__(self, other) -> float:
        return float(np.dot(self.__args, other.__args))

    def vector_norm(self) -> Union[int, float]:
        return np.linalg.norm(self.__args)

    @property
    def args_as_np(self):
        return np.array(list(self.__args))

    @property
    def dimension(self):
        return self.__dimension

    def __getitem__(self, coord) -> Union[int, float]:
        return self.__args[coord]

    def __setitem__(self, key, value) -> None:
        assert (isinstance(value, int) or isinstance(value, float))
        self.__args[key] = value

    def __len__(self):
        return self.__dimension

    def __iadd__(self, other):
        self.__args += other.__args
        return self

    def __add__(self, other):
        sum_coords = self.__args + other.__args
        return MyVector(self.dimension, *sum_coords)

    def __sub__(self, other):
        sum_coords = self.__args - other.__args
        return MyVector(self.dimension, *sum_coords)

    def __isub__(self, other):
        self.__args -= other.__args
        return self

    def __eq__(self, other):
        return self.__args == other.__args

    def __lt__(self, other):
        return self.vector_norm() < other.vector_norm()

    def __ge__(self, other):
        return self.vector_norm() >= other.vector_norm()