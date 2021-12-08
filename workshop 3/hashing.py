from typing import Iterable




"""
password -> [password] # ცუდია

password -> [123k1v2jh34gj1h2vg4vj1b2hg4vb12v34gj]


a -> b
b -> c
luka -> mvlb
"""





def დაჰეშე(char: str) -> str:
    if char == 'Z' or char == 'z':
        return chr(ord(char) - 25) # a - A, 122 - 25 ->  97 , 90 - 25 -> 65
    return chr(ord(char) + 1) # a 97 + 1 -> 98 

def dehash(char: str) -> str:
    if char == 'a' or char == 'A':
        return chr(ord(char) + 25)
    return chr(ord(char) - 1)


def make_hash(hashable: str) -> str:
    """
        A - Z ->  65 - 90
        a - z ->  91 - 122
    """
    if not isinstance(hashable, str):
        print('hashable must be a string!')
        return
    
    hashed_chars: list[str] = [] # a , v, v,b ,we

    for char in hashable:
        # ord აბრუნებს ASCII კოდს
        char_ascii = ord(char)
        if not (ord('a') <= char_ascii and char_ascii <= ord('z')) and not (ord('A') <= char_ascii and char_ascii <= ord('Z')):
            print('hashable must contain only letters [a-z and A-Z]')
            return

        hashed_chars.append(დაჰეშე(char))
    return ''.join(hashed_chars) # ['a', 'b'] -> ab

def read_hash(hashed: str) -> str:
    dehashed_chars: list[str] = []

    for char in hashed:
        dehashed_chars.append(dehash(char))
    
    return ''.join(dehashed_chars)

password = make_hash("password")

print(password)

print(read_hash(password))

def find(item: any, iterable: Iterable) -> int:
    """ -1 if element not found else you will get index of it """
    # Iterable-ები არიან str, list, tuple, და სხვა
    i: int = 0
    for element in iterable:
        if element == item:
            return i
        i += 1
    else:
        return -1

print(find(4, [1, 2, 3, 4, 6]))

print(find('a', 'helloa'))


print('\n\n\n\n\n\n')

def ჩაამატე(ლისი_სადაც_უნდა_ჩაამატო: list, ელემენტი):
    ლისი_სადაც_უნდა_ჩაამატო.append(ელემენტი)

სიტყვა = "my password" # itrebale 
დაჰეშილი_სიტყვა = []

for ასო in სიტყვა:
    ჩაამატე(დაჰეშილი_სიტყვა, დაჰეშე(ასო))

print(''.join(დაჰეშილი_სიტყვა))
