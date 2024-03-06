class Rectangle:
    def __init__(self, base: int | float, height: int | float) -> None:
        self.base = base
        self.height = height

    def calculate_area(self) -> int | float:
        return self.base * self.height

    def calculate_perimeter(self) -> int | float:
        perimeter = (self.base * 2) + (self.height * 2)
        return perimeter


rectangle1 = Rectangle(5, 10)
print(rectangle1.calculate_area())
print(rectangle1.calculate_perimeter())
