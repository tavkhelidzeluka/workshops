
class Car:
    def __init__(self, brand: str, seats: int, price: float) -> None:
        self.brand: str = brand
        self.seats: int = seats
        self.price: float = price

    def print(self):
        try:
            print(self.brand, self.seats, self.price)
        except AttributeError:
            print('Errori gavarda da davichire')
            print(self.brand, self.price)
