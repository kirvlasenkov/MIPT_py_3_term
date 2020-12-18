from typing import Optional


class Animal:
    name: Optional[str] = None
    age: Optional[int] = None

    def __init__(self, name: str = name, age: int = age) -> None:
        if isinstance(name, str) and isinstance(age, int):
            self._name = name
            self._age = age

        else:
            raise ValueError("wrong data type")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        assert isinstance(new_name, str)
        self._name = new_name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        assert isinstance(new_age, int)
        self._age = new_age

    def make_sound(self):
        return self.sound


class Zebra(Animal):
    _sound: Optional[str] = "zezeze"
    name: Optional[str] = None
    age: Optional[int] = None

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    @property
    def sound(self):
        return self._sound


class Dolphin(Animal):
    _sound: Optional[str] = "dodododo"
    _name: Optional[str] = None
    _age: Optional[int] = None

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    @property
    def sound(self) -> str:
        return self._sound


if __name__ == "__main__":
    zoo = []
    zebra = Zebra("Bob", 15)
    dolphin = Dolphin("Scott", 10)

    zoo.append(zebra)
    zoo.append(dolphin)

    for animal in zoo:
        print(animal.make_sound())
