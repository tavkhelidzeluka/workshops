# a: list[int] = [1, 2, 3, 2, 5345, 55]
# b: list[int] = [255, 552, 1, "bar"]

# # len(a)

# # len(a) - 1
# print(a)
# a.extend(b)

# print("a after extension: ", a)

# a.remove("bar")
# print("a after removal of \"bar\": ", a)

# a.pop(-1)

# del a[0] # pointer
# a.insert(0, 5)

# print('a = ', a)

# a.clear() # გაასუფთავებს    

# print(a)
# del a # შლის ცვლადს

# a - z [97, 122]
# A - Z [65, 91]

# name = "Gio"
# age = 27

# if (name.lower() == "mari" or name.lower() == "gio") and age == 27:
#     print(f"{name} successfully registered!")
# else:
#     print("leave")


#    0  1  2  3
a = [5, 2, 4, 1, 6, 0, 8, 2, 3, 4, 5]

# for i in range( 2, len(a) ):
#     print(a[i])
print(a.index(4))
dublicates = [] # 2


# print()
# for element in a[a.index(4):]:
#     print(element)

# იპოვეთ მასივში (ლისტი) დუბლიკატები დაპრინტეთ

for element in a:
    for dub_el in dublicates:
        if dub_el == element:
            print(f'{element} has a doppleganger!')

    dublicates.append(element)

index = 0

for i in range(len(a)):
    if a[i] == 5:
        index = i
        break
        

print(index, a.index(5))

for element in a:
    if element % 2 == 1:
        print("list contains odd number")
        break

print("\nprint all even numbers:")
for e in a:
    if e % 2 == 1:
        continue
    print(e)


# mutable, immutable
print("\nmuttable, immutable: ")
name = "Luka" # immutable
my_list = list( (1, 2, 3, 4) )
my_tuple = (1, 2, 3)



print(type(my_tuple))

i = 0

while (i < len(my_tuple)):
    print(my_tuple[i])
    i += 1