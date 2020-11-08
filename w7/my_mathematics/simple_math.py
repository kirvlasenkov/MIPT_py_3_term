from typing import Tuple, Union
import math
import cmath
import numpy as np


class MyMath:
    '''
    Simple class with some
    mathematical operations.
    '''
    pi: float = 3.14
    _complex: bool = False  # Инкапсуляция

    @staticmethod
    def sin(x: Union[int, float]) -> Union[int, float]:
        '''
        Copy of standard sine function.
        Just need to demonstrate static method philosophy.
        :param x: definite point
        :return: sin(x)
        '''
        return np.sin(x)

    @classmethod
    def complex(cls):
        return cls._complex

    @classmethod
    def sqrt(cls, x: Union[int, float]) -> Union[Union[int, float],
                                                 Tuple[Union[int, float], Union[int, float]]]:

        if x < 0:
            if cls.complex() is False:  # Элементы полиморфизма
                raise ValueError("Incorrect number! You are located in Real field")
            else:
                result: complex = cmath.sqrt(x)
                return result.real, result.imag

        else:
            return math.sqrt(x)


class MyComplexMath(MyMath):  # Наследование
    '''
    Variation of MyMath for complex field.
    '''
    _complex: bool = True  # Наследование и инкапсуляция
