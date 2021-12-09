# from workshop_4 import shekribe

# print(shekribe(1, 2))

# print(gaamravle(2, 2))

import random


print(random.randint(0, 10))
print(random.sample([1, 2, 3, 4, 5], 4))
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)
print(random.choice([1, 2, 4, 5, 5, 3]))

"""
70

55 # naklebia
90 # metia
80 # metia
71 # metia
70 # gamoicani

"""
import time

a = []
for i in range(10000000000):
    a.append(i)

time.sleep(20)