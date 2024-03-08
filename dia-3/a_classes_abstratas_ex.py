from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def print_role(self):
        pass


class Seller(Person):
    def print_role(self):
        return 'Meu cargo é de vendedor'


class Manager(Person):
    def print_role(self):
        print('Meu cargo é de gerente')


vendedor = Seller()
print(vendedor.print_role())

gerente = Manager()
gerente.print_role()
