from math import sqrt
from typing import Union


class Shape:
    """
    Abstract class. Main part of
    the geometry figure hierarchy
    """
    _width = 0
    _length = 0

    def __init__(self, width: Union[int, float],
                 length: Union[int, float]) -> None:
        """
        constructor of the abstract figure
        :param width:
        :param length:
        """
        self._width = width if width >= 0 else -1
        self._length = length if length >= 0 else -1

    @property
    def width(self) -> Union[int, float]:
        if self._width == -1:
            raise ValueError("wrong data")
        else:
            return self._width

    @width.setter
    def width(self, new_width) -> None:
        if (isinstance(new_width, int) or isinstance(new_width, float)) and new_width >= 0:
            self._width = new_width
        else:
            raise ValueError("wrong data!!!")

    @property
    def length(self) -> Union[int, float]:
        if self._length == -1:
            raise ValueError("wrong data")
        else:
            return self._length

    @length.setter
    def length(self, new_length) -> None:
        if (isinstance(new_length, int) or isinstance(new_length, float)) and new_length >= 0:
            self._width = new_length
        else:
            raise ValueError("wrong data!!!")

    @property
    def area(self) -> Exception:
        raise NotImplementedError()


class Triangle(Shape):
    """
    triangle - a simplex in a
    2-dimensional space.
    A progeny of a Shape.
    """
    _side_1 = 0
    _side_2 = 0
    _side_3 = 0

    def __init__(self, side_1: Union[int, float],
                 side_2: Union[int, float],
                 side_3: Union[int, float]) -> None:
        """
        constructor of a triangle
        :param side_1: length of the first triangle side
        :param side_2: length of the second triangle side
        :param side_3: length of the third triangle side
        """
        self._side_1 = side_1 if side_1 >= 0 else -1
        self._side_2 = side_2 if side_2 >= 0 else -1
        self._side_3 = side_3 if side_3 >= 0 else -1

    @property
    def area(self) -> Union[int, float]:
        """
        returns area of a triangle
        :return: area of a triangle
        """
        p = (self._side_1 + self._side_2 + self._side_3) / 2

        return (sqrt(p * (p - self._side_1)
                     * (p - self._side_2)
                     * (p - self._side_3)))


class Rectangle(Shape):
    """
    Rectangle - Hyperrectangle in a 2-dimensional space.
    Progeny of a Shape
    """

    def __init__(self, width, length) -> None:
        """
        Constructor of a Rectangle-object
        """
        super().__init__(width, length)

    @property
    def area(self) -> Union[int, float]:
        return self.width * self.length


if __name__ == "__main__":
    rectangle = Rectangle(-10, 10)
    rectangle.length = -20
    rectangle.width = 15
    print("for rectangle",
          "area: ", rectangle.area,
          "width: ", rectangle.width,
          "length: ", rectangle.length,
          sep='\n')

    triangle = Triangle(1, 1, 1)
    print("area of a triangle:\n", triangle.area)
