# initialization of a variable
VARIABLE: str = 'I\'m a global variable, I exist until program ends or someone frees me from memory'

print(VARIABLE)

# del VARIABLE # ცვლადი წავშალეთ მეხსიერებიდან
# print(VARIABLE) # ცვლადი აღარ არსებობს მეხსიერებაში და ვერ მივწვდებით

print(VARIABLE.islower())


def locals():
    variable = 'I\'m local variable, I exist only in a call of a function'

    print(variable)

    del variable


locals()