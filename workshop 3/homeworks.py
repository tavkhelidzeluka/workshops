"""
შექმენით 10 ელემენტიანი ლისტი და შეავსეთ 
კლავიატურიდან შეტანილი მთელი რიცხვებით. 
შემდეგ თითოეული ელემენტი ლისტში აიყვანეთ 
მომდევნო ინდექსზე მდგომი ელემენტის ხარისხში 
(ბოლო ინდექსზე მდგომი ელემენტი აიყვანეთ პირველი ელემენტის ხარისხში)


2, 2, 3, 4, 5, 6, 2
"""

# my_list: list[int] = []

# for _ in range(5):
#     my_list.append(int(input("Enter number: ")))

# # last_elem = my_list[-1]
# # my_list[-1] **= my_list[0]

# for i in range(len(my_list) - 1):
#     my_list[i] **= my_list[i + 1]


# my_list[-1] **= my_list[0]

# print(my_list)


"""
შექმენით ორი მასივი (ლისტი) ორივე შეავსეთ 1000 - 1000 ელემენტით, 
კენტები 1 მასივში ლუწები მეორეში. შემდეგ კენტების მასივის ელემენტები აიყვანეთ 
ლუწი მასივის ელემენტების ხარისხში odd_element ^ (even_element - 1)/ even_element^2.
და ბოლოს ლუწების მასივის თითოეული ელემენტი გაყავით კენტების ელემენტებზე. 
(P.S ორივე მასივის ელემენტები უნდა შეიცვალოს!) 
"""

"""
truthy:
1, 2, 2, 3,-1 
1.2
"ლუკა"
" "

falsy:
[]
()
{}
''
0
None

"""

# list comprehension
# even_numbers = [num for num in range(2, 2002, 2)]
# odd_numbers = [num for num in range(1, 2000, 2)]

# for i in range(1, 2000, 2): # n
#     odd_numbers.append(i)

# print(even_numbers[:20])
# print(odd_numbers[:20])

# odd_element ^ (even_element - 1)/ even_element^2

# def do_my_thing(odd_element, even_element):
#     return odd_element ** ((even_element - 1)/ (even_element ** 2))


# for i in range(len(odd_numbers)):
#     odd_numbers[i] **= ((even_numbers[i] - 1) / (even_numbers[i] ** 2))

# for i in range(len(odd_numbers)):
#     even_numbers[i] /= odd_numbers[i]

# odd_numbers = [do_my_thing(odd_numbers[i], even_numbers[i]) for i in range(len(even_numbers))]
# odd_numbers = [do_my_thing(odd_num, even_num) for odd_num, even_num in zip(odd_numbers, even_numbers)]

# for odd_element, even_element in zip(odd_numbers, even_numbers):

#     print(odd_element, even_element)
#     break

# print(odd_numbers)
# print(even_numbers)



"""
მომხმარებელს კლავიატურიდან შემოატანინეთ რიცვხი, გაარკვიეთ 
რიცხვი ლუწია თუ კენტი (პროგრამამ უნდა იმუშაოს ნებისმიერ
მთელ რიცხვზე რა ზომისაც არ უნდა იყოს ის. გაითვალისწინეთ 
პითონში რიცხვის მაქსიმალური ზომა დამოკიდებულია თქვენს ოპერატიულზე, ამიტომაც სხვა გზა უნდა იპოვოთ)
"""
import time
num = input("enter number: ")

time.sleep(1000)
if int(num[-1]) % 2:
    print("კენტია")
else:
    print("ლუწია")

# array 

