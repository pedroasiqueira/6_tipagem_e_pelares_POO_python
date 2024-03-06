class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def make_sound(self) -> str:
        return f'{self.name} fazendo som'


class Mammal(Animal):
    def breastfeed(self) -> str:
        return f'{self.name} amamentando'


class Dog(Mammal):
    def bark(self) -> str:
        return f'{self.name} Au au!'


thor = Dog('Thor')
print(thor.make_sound())
print(thor.breastfeed())
print(thor.bark())
