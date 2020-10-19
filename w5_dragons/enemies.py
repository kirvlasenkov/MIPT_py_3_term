# coding: utf-8
# license: GPLv3

from scipy import integrate
from gameunit import Attacker
from random import choice, randint
from typing import Union, List, Tuple, Optional
import numpy as np


class Enemy(Attacker):
    """
    Abstract class for the declaring enemy group.
    """

    @property
    def cheat(self):
        return self._cheat_code


def generate_random_enemy():
    """
    Picks a random enemy from enemy_types list
    and returns one.
    """
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number) -> List:
    '''
    returns a list with
    a random sequence of enemies

    :param  enemy_number: number of enemies
    '''
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    '''
    Superclass for dragons.
    '''

    def set_answer(self, answer) -> None:
        '''
        Set an actual answer received from user.
        :param answer: user answer
        '''
        self.__answer = answer

    def check_answer(self, answer):
        """
        Checks is it user answer correct or not.
        "param answer: user answer
        """
        return answer == self.__answer

    def question(self):
        '''
        Problem, which user should solve.
        '''
        raise NotImplementedError


class GreenDragon(Dragon):
    '''
    Dragon, which produce mathematical problems,
    connected with addition.
    '''

    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'green'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + ' + ' + str(y)
        self.set_answer(x + y)
        return self.__quest

    _cheat_code = -1


class RedDragon(Dragon):
    '''
    Dragon, which produce mathematical problems,
    connected with subtraction.
    '''

    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'red'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + ' - ' + str(y)
        self.set_answer(x - y)
        return self.__quest

    _cheat_code = -2


class BlackDragon(Dragon):
    '''
    Dragon, which produce mathematical problems,
    connected with multiplication.
    '''

    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'black'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

    _cheat_code = -3


class DifferentialDragon(Dragon):
    '''
    Dragon, which produce mathematical problems,
    connected with differential calculus.
    '''

    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'differential'
        self._cheat_code = -4

    @staticmethod
    def polynomial(x: Union[int, float]) -> Tuple[Union[int, float], List[int]]:
        """
        Produce polynomial with real random coefficients.
        Returns value of poly derivative in definite point, list of original poly
        :param x: definite point
        :degree: degree of a polynomial
        """
        degree = randint(0, 5)
        poly_coef = [randint(0, 20) for _ in range(degree + 1)]
        poly_der_coef = np.polyder(poly_coef)
        value = 0
        for i in range(len(poly_der_coef)):
            value += poly_der_coef[i] * x ** i

        return (value, poly_coef)

    def question(self):
        func_type = choice(["sin", "cos", "real polynomial"])

        if func_type == 'sin':
            x = choice(np.arange(0, 2 * np.pi, np.pi / 3))
            self.__quest = "sin(x) at point {}".format(x)
            self.set_answer(np.cos(x))

        if func_type == 'cos':
            x = choice(np.arange(0, 2 * np.pi, np.pi / 3))
            self.__quest = "cos(x) at point {}".format(x)
            self.set_answer(-np.sin(x))

        if func_type == 'real polynomial':
            x = randint(0, 100)
            answer, poly_coefs = DifferentialDragon.polynomial(x)
            self.__quest = "solve derivative value of polynomial in" \
                           " {} with coefficients: {}".format(x, poly_coefs)
            self.set_answer(answer)

        return self.__quest


class IntegralDragon(Dragon):
    '''
    Dragon, which produce mathematical problems,
    connected with integral calculus.
    '''

    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'integral'

    # FIXME Данила, реализуй меня!!!, я интеграл Римана одной переменной на отрезке!!!
    # FIXME Hint: юзай scipy.integrate

    _cheat_code = -5

    pass


class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

    def __init__(self):
        self._health = 250
        self._attack = 20
        self._color = "ogre"

    def question(self):
        pass

    _cheat_code = -6


enemy_types = [GreenDragon, RedDragon, BlackDragon,
               DifferentialDragon, IntegralDragon, Troll]
