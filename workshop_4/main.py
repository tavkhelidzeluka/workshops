# my_file = open('./test.txt', 'r')

# names = my_file.read()
# print(repr(names))

# name_list: list[str] = []

# for name in names.split(','):
#     name_list.append(name.strip())

# my_file.close()

# my_file = open('./test.txt', 'w+')

# name_list.append("test user")

# for name in name_list[:-1]:
#     my_file.write(f'{name}, ')

# my_file.write(f'{name_list[-1]}')

# print(name_list)

# my_file.close()


# my_file = open('./test.txt', 'r')

# for line in my_file.readlines():
#     print(line, end='')

# my_file.close()


# removing
import os

# if os.path.exists('./prices.txt'):
#     os.remove('./prices.txt')


# # create file
# open('./prices.txt', 'x')



if not os.path.exists('./prices.txt'):
    open('./prices.txt', 'x')


import time


# while True:
#     print(' o ')
#     print('/|\ ')
#     print('/ \\')
#     time.sleep(0.5)

#     os.system('cls')


#     print('  o ')
#     print('/// ')
#     print('/\\')
#     time.sleep(0.5)

#     os.system('cls')


# from pathlib import Path


# BASE_DIR = Path().parent.resolve()

# print(BASE_DIR / 'workshop 4' / 'test.txt')


# n = [-255252, -1, -2, -3, -4]
# m = [0]

# # for i in range(1, len(n)):
# #     if n[i] > m:
# #         m = n[i]

# for num in n[1:]:
#     if num > m:
#         m = num

# print(m)

from typing import Dict, Union

person: Dict[str, Union[str, int, list[str]]] = {
    'name': "John",
    'age': 56,
    'friends': ["jane", "Adolf"]
}

# l: list[Union(str, int)] = [1, "tet", 123 , "wrew"]

persons = [
    {
        'name': "John",
        'age': 56,
        'friends': ["jane", "Adolf"]
    },
    {
        'name': "Jane",
        'age': 56,
        'friends': ["ane", "Adolf"]
    }
]

print(person['friends'])


from second import shekribe


print(shekribe(5, 6))
