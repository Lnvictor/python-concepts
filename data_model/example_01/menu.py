from collections import namedtuple
from re import M


Dish = namedtuple('Dish', 'name country type')


class FrenchMenu():
    def __init__(self) -> None:
        self.dishes = [Dish('petit gateau', 'French', 'dessert')]

    def __len__(self):
        return len(self.dishes)

    def __getitem__(self, pos):
        return self.dishes[pos]


class ItalianMenu():
    def __init__(self) -> None:
        self.dishes = [Dish('lasagna', 'Italian', 'pasta')]
    
    def __len__(self):
        return len(self.dishes)

    def __getitem__(self, pos):
        return self.dishes[pos]


class BrazilianMenu():
    def __init__(self) -> None:
        self.dishes = [Dish('Feijoada', 'Brazil', 'melhor comida do mundo')]

    def __len__(self):
        return len(self.dishes)

    def __getitem__(self, pos):
        return self.dishes[pos]


if __name__ == '__main__':
    print("Escolha qual culinaria vc quer experimentar: ")
    print("1. Italiana")
    print("2. Brasileira")
    print("3. Francesa")
    choice = int(input("Digite sua opção: "))

    options = {
        1: ItalianMenu(),
        2: BrazilianMenu(),
        3: FrenchMenu(),
    }

    print(f"Pratos disponiveis: {options[choice][0]}")