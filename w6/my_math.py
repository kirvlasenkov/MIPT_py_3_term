from typing import Tuple, Union
import math
import cmath


class MyMath:
    '''
    Simple class with some
    mathematical operations.
    '''
    pi: float = 3.14
    __complex: bool = False  # Инкапсуляция

    @staticmethod
    def sin(x: Union[int, float]) -> Union[int, float]:
        '''
        Copy of standard sinus function.
        Just for demonstrate static method philosophy.
        :param x: definite point
        :return: sin(x)
        '''
        return math.sin(x)

    @classmethod
    def complex(cls):
        return cls.__complex

    @classmethod
    def sqrt(cls, x: Union[int, float]) -> Union[Union[int, float],
                                                 Tuple[Union[int, float], Union[int, float]]]:

        if x < 0:
            if cls.complex() == False:  # Элементы полиморфизма
                raise ValueError("Incorrect number! You are located in Real field")
            else:
                result: complex = cmath.sqrt(x)
                return (result.real, result.imag)

        else:
            return math.sqrt(x)


class MyComplexMath(MyMath):  # Наследование
    '''
    Variation of MyMath for complex field.
    '''
    __complex: bool = True  # Наследование и инкапсуляция


if __name__ == "__main__":
    real_number = MyMath()
    complex_number = MyComplexMath()

    # Simple test for sinus
    print("sinus work:\n for complex: {}\n for real: {}\n".
          format(complex_number.sin(2 * MyMath.pi),
                 real_number.sin(MyMath.pi / 2)))

    # Simple test for sqrt
    try:
        neg_comp_sqrt = MyComplexMath.sqrt(-10)
        pos_comp_sqrt = MyComplexMath.sqrt(10)
        pos_real_sqrt = MyMath.sqrt(10)
        neg_real_sqrt = MyMath.sqrt(-10)
        print(neg_real_sqrt)
    except Exception:
        print("ohh, smth gone wrong:(")
    else:
        print("everything is alright")

    '''
    Мы использовали классовый методы, так как это позволило нам отслеживать, 
    чему равно у конкретного класса поле __complex. Static method здесь точно не был бы
    уместен, так как по сути он никак не ссылается и не указывает на то, что это метод 
    конкретного класса или экземпляра класса. 
    '''
