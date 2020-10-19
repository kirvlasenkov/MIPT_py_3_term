# coding: utf-8
# license: GPLv3
from gameunit import Attacker
from typing import Optional, Union


class Hero(Attacker):
    '''
    Class of the positive character.
    Controlled by the user.
    '''

    # boundary experience quantity for level up
    __exp_boundary: Union[int, float] = 100

    # current level of a hero
    _level: int = 0

    def __init__(self, name: Optional[str] = None) -> None:
        '''
        Default constructor.
        :param name: hero name
        '''
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("wrong data type!!! name must be a string-type")

        self._health: Union[int, float] = 100
        self._attack: Union[int, float] = 50
        self._experience: int = 0

    def attack(self, target: Optional[str] = None) -> None:
        super().attack(target)

    def level_up(self) -> None:
        """
        Realization of the leveling up.
        """
        if self._experience >= self.__exp_boundary:
            self._health *= 0.2
            self._attack *= 0.1
            self._experience = 0
            self.__exp_boundary += 50
            self._level += 1
        else:
            print("you don't have enough experience.\
             required for upgrade: {}".format(self.__exp_boundary - self._experience))

    @property
    def level(self):
        '''
        simple level descriptor (only for reading)
        '''
        return "your current level is: " + str(self._level)
