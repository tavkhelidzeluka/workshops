# Classes
import wina
from car import Car
from animal import Animal, Specie
from user import User


def func(y):
    return lambda a: a * y



if __name__ == '__main__':
    # print(__name__)
    # print(wina.__name__)

    # y = 5

    # x = lambda c: c + 1

    # print(x())

    # x = func(6) # lambda a: a * 6
    # print(x(2))

    # [1, 2 , 3, 4].sort(key=lambda a, b: print(a, b))

    # instantiate
    # my_car = Car('mercedes', 4, 50000)
    # friend_car = Car('BMW', 6, 50000)

    # # print(my_car.brand, my_car.price, my_car.seats)
    # # print(friend_car.brand, friend_car.price, friend_car.seats)

    # my_car.print()

    # my_car.brand = 'Tesla'

    # # del my_car.price
    # # my_car.price = 6
    # # my_car.owner = "luka"
    # # print(my_car.owner)

    # my_car.print()
    # friend_car.print()


    """ Animal """
    # birds = Specie("birds")

    # eagle = Animal(birds, "Hunter", 2)
    # penguin = Animal(birds, "Happy", 2)



    # print(eagle)
    # eagle.move()
    # print(penguin)
    # penguin.move()

    # # accessing static methods
    # print(penguin.can_eat)
    # print(Animal.can_eat)

    """ User """

    users: list[User] = []

    users.append(User("test123", 'password'))

    print(users[0].password)