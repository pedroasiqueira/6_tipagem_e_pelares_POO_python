from abc import ABC, abstractmethod
from math import pi


class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimetro(self):
        ...


class Quadrado(FiguraGeometrica):
    def __init__(self, lado) -> None:
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4


class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(FiguraGeometrica):
    def __init__(self, raio) -> None:
        self.raio = raio

    def area(self):
        return pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * pi * self.raio


quadrado = Quadrado(2)
print(quadrado.area())
print(quadrado.perimetro())

retangulo = Retangulo(2, 4)
print(retangulo.area())
print(retangulo.perimetro())

circulo = Circulo(3)
print(circulo.area())
print(circulo.perimetro())
