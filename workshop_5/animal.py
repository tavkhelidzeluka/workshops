class Specie:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return self.name


class Animal:
    can_eat = True

    def __init__(self, specie: Specie, name: str,  leg_count: int) -> None:
        self.name = name
        self.specie = specie # composition
        self.leg_count = leg_count
    
    @staticmethod
    def move():
        print("moving")
    
    def __str__(self) -> str:
        return f'name: {self.name}, specie: {self.specie}, legs: {self.leg_count}'