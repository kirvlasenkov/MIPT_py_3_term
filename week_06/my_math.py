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



if __name__ == "__main__":
    real_number = MyMath()
    complex_number = MyComplexMath()

    # Simple test for sinus
    print("sine work:\n for complex: {}\n for real: {}\n".
          format(complex_number.sin(2 * MyMath.pi),
                 real_number.sin(MyMath.pi / 2)))

    # Simple test for sqrt on positive value
    try:
        pos_comp_sqrt = MyComplexMath.sqrt(10)
    except Exception:
        print("ohh, smth gone wrong with sqrt on positive")
    else:
        print("positive complex sqrt: ", complex(pos_comp_sqrt))
        print("everything is alright with complex sqrt on positive (expected result)\n")

    try:
        pos_real_sqrt = MyMath.sqrt(10)
    except Exception:
        print("ohh, smth gone wrong with sqrt on positive")
    else:
        print("positive real sqrt: ", pos_real_sqrt)
        print("everything is alright with real sqrt on positive (expected result)\n")


    try:
        neg_comp_sqrt = MyComplexMath.sqrt(-10)
    except Exception:
        print("ohh, smth gone wrong with sqrt on negative")
    else:
        print("negative complex sqrt: ", neg_comp_sqrt)
        print("everything is alright with sqrt on negative (expected result)\n")

    # Simple test for sqrt on negative value
    try:
        neg_real_sqrt, v = MyMath.sqrt(-10)
    except Exception:
        print("ohh, smth gone wrong with sqrt on negative (expected result)\n")
    else:
        print("negative real sqrt: ", neg_real_sqrt)
        print("everything is alright with sqrt")

    # Simple test for sine:
    try:
        real_sin = MyMath.sin(1)
    except Exception:
        print("ohh, smth gone wrong with sine")
    else:
        print("sine on the real field:", real_sin)
        print("everything is alright with sine (expected result)\n")

    try:
        complex_sin = MyComplexMath.sin(1 + 1j)
    except Exception:
        print("ohh, smth gone wrong with sine")
    else:
        print("sine on the complex field:", complex_sin)
        print("everything is alright with sine (expected result)\n")



    '''
    Мы использовали классовыe методы, так как это позволило отслеживать, 
    чему равно у конкретного класса поле __complex. Static method здесь точно не был бы
    уместен, так как по сути он никак не ссылается и не указывает на то, что это метод 
    конкретного класса или экземпляра класса, это лишь реализации функции внутри класса. 
    '''
