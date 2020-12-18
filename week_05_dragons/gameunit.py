# coding: utf-8
# license: GPLv3
from typing import Optional


class Attacker:
    '''
    Global abstract class.
    '''
    _health: Optional[int] = None
    _attack: Optional[int] = None

    def attack(self, target) -> None:
        '''
        Abstract attacking function.
        :param target: target unit name
        '''
        target._health -= self._attack

    def is_alive(self) -> bool:
        '''
        Returns life's state of a game unit
        '''
        return self._health > 0
