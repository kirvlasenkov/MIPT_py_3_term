from typing import Optional


class Mother:
    _name: Optional[str] = None
    _age: Optional[int] = None

    def __init__(self, name: str, age: int) -> None:
        """
        Constructor of Mother class
        :param name: mother's name
        :param age: mother's age
        """
        assert (isinstance(name, str) and isinstance(age, int))
        self._name = name
        self._age = age

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

    def __str__(self) -> str:
        return "name: " + self.name + "; age:  " + str(self.age)


class Daughter(Mother):
    _mother: Optional[str] = None
    _name: Optional[str] = None
    _age: Optional[int] = None

    def __init__(self, name: str, age: int, mother: str) -> None:
        assert isinstance(mother, str)
        super().__init__(name, age)
        self._mother = mother

    def __getattr__(self, item):
        return self.__dict__[item]

    @property
    def mother(self):
        return self._mother

    @mother.setter
    def mother(self, new_mother):
        raise ValueError("you can't change your mom!!!")

    def __str__(self):
        return "child: {} {} years old with mother {}".format(self.name, self.age, self.mother)


if __name__ == "__main__":
    mother = Mother("Anya", 10)
    mother.name = "Anna"
    mother.age = 34
    print(mother)

    child = Daughter("Manya", 10, "Alya")
    child.name = "Masha"
    print(child)
