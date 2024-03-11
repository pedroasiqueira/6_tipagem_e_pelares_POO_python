from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, price) -> None:
        self._price = price

    @abstractmethod
    def print_price(self):
        raise NotImplementedError(
            'Classes derivadas de Product precisam implementar o preço')


class Book(Product):
    def __init__(self, price) -> None:
        super().__init__(price)

    def print_price(self):
        print(f'O preço do livro é: {self._price}')


livro = Book(10)

livro.print_price()
