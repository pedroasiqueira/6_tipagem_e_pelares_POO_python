class Product:
    def __init__(self, name: str, price: float) -> None:
        self._name = name
        self._price = price

    def get_description(self):
        pass

    def get_price(self):
        pass


class Book(Product):
    def __init__(self, name: str, price: int, author: str) -> None:
        super().__init__(name, price)
        self._author = author

    def get_description(self) -> str:
        return f'{self._name} author: {self._author}'

    def get_price(self) -> float:
        return self._price


class DVD(Product):
    def __init__(self, name: str, price: int, direction: str) -> None:
        super().__init__(name, price)
        self._direction = direction

    def get_description(self):
        return f'{self._name} dirigido por {self._direction}'

    def get_price(self):
        return self._price


book = Book("O Senhor dos Anéis", "J.R.R. Tolkien", 29.99)
dvd = DVD("O Poderoso Chefão", "Francis Ford Coppola", 19.99)


def print_details(clss):
    print(f'{clss.get_description()}, preço: {clss.get_price()}')


print_details(book)
print_details(dvd)
