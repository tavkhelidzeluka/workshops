# primitive type:
from sys import getsizeof
from typing import AbstractSet



int, bool, float

# complex type:
str, list, tuple, dict, set

# class MyClass:
#     i: list[int] = [] # static attribute


#     @staticmethod
#     def bar() -> None:
#         print("bar was called")

#     def foo(self):
#         print("foo was called")


# a = MyClass() # instantiate -> creates object of class
# b = MyClass()
# c = MyClass()

# print(a)

# a.foo()
# b.foo()

# print(a.i)
# print(b.i)
# print(c.i)
# print(MyClass.i)

# a.bar()
# b.bar()
# MyClass.bar()


# class Dog:
#     kind = 'German Shepherd'

#     def __init__(self, name: str, tricks: list[str] = []) -> None:
#         self.tricks: list[str] = tricks
#         self.name: str = name

#     @staticmethod
#     def bark():
#         print("wof wof")

#     def add_trick(self, trick: str):
#         self.tricks.append(trick)


# lucy = Dog('Lucy', ['front flip'])
# gela = Dog('Xenia')

# gela.name = "Gela"

# print(lucy.name)
# print(gela.name)

# Dog.bark()
# lucy.bark()
# gela.bark()


# lucy.add_trick('roll over')
# gela.add_trick('jumping')

# print(lucy.tricks)
# # print(Dog.tricks)
# print(gela.tricks)

# print(gela.kind)
# print(Dog.kind)


# class ChocolateFactory:
#     def __init__(self, title: str) -> None:
#         self.title = title
#         self.__products: list[str] = []

#     def add_product(self, product: str):
#         if not isinstance(product, str):
#             print('product must be a str type')
#             return

#         self.__products.append(product)

#     def display_products(self):
#         print(self.__products)


# rf: ChocolateFactory = ChocolateFactory('Russian')
# gf: ChocolateFactory = ChocolateFactory('Georgian')

# rf.add_product(5)
# rf.add_product('datvi shokoladi')

# gf.add_product('Barambino')
# gf.add_product('Mamalo')


# rf.display_products()
# gf.display_products()

# print(isinstance(gf, ChocolateFactory))
from abc import ABC, abstractmethod


# class AbstractPerson(ABC):
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
    
#     @abstractmethod
#     def shout(self):
#         pass


# class Student(AbstractPerson):
#     def shout(self):
#         print('oe bicho')


# class Lecturer(AbstractPerson):
#     def shout(self):
#         print('excuse me')



# niko = Student('niko', 25)

# niko_lecturer = Lecturer('niko', 25)
# mari = Lecturer('mari', 37)

# people: list[AbstractPerson] = []
# print(isinstance(niko, AbstractPerson))



# print('niko is not niko lecturer: ', niko is not niko_lecturer)

# print(niko.name, mari.name)


# niko.shout()
# niko_lecturer.shout()


""" Animals """

class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def swim():
        pass

    @abstractmethod
    def eat(self):
        pass


class Mammal(Animal):
    def __init__(self, name: str, feet: int) -> None:
        super().__init__(name)
        self.feet: int = feet



    def swim(self):
        print('wyap wyup')
    
    def eat(self):
        print('nom nom')
    
    def walk(self):
        print('baj baj')


class Fish(Animal):

    def swim(self):
        print('fish swmin')
    
    def eat(self):
        print('fish eat')

class Bird(Animal):
    def swim(self):
        print('bird swim')
    
    def eat(self):
        print('bird eat')


animals: list[Animal] = [
    Fish('bobo'), Fish('bubu'),
    Bird('parrot'), Mammal('mai', 4)
]


for animal in animals:
    print('~~~~~~~~~~~~~~')
    print(animal.name)
    animal.swim()
    animal.eat()
    print('~~~~~~~~~~~~~~')

print(animals[3].feet)

if __name__ == '__main__':
    pass
