def add_two_numbers(num1: int, num2: int) -> int:
    return num1 + num2


print(add_two_numbers(1, 2.0))


class Person:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age = age
        self.height = height
