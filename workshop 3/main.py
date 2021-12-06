def figure_type_and_value(my_var):
    print(type(my_var), my_var)


# figure_type_and_value(5)
# figure_type_and_value("hello ")
# figure_type_and_value(True)


def greet(name: str):
    print(f'hello {name}')


# greet("luka")
# greet("Nika")
# greet("Nino")


def is_even(my_list: list[float]):
    for element in my_list:
        if element % 2 == 0:
            print('list contains at least one even number!')
            break
    else:
        print('list contains no even number')


# is_even([1, 2 ,3, 4, 5, 6, 6])
# is_even([9, 5, 3, 1, 2, 5, 6])
# is_even([9, 5, 3, 1, 1, 5, 7])
global_var = 0


def gamoitane_lamazad(name: str, age: int, gender: bool) -> None:
    global global_var
    global_var += 1
    if not isinstance(age, int):
        print("age must be an int!")
        return

    gen_name: str = "Male"

    if gender == False:
        gen_name = "Female"

    print(f'I\'m {name}, {age} years old, {gen_name}')

# void function <=> -> None
def print_globals():
    print('from function print globals', global_var)

gamoitane_lamazad(20, "Luka", True)
gamoitane_lamazad("NIno", 25, False)

print(f"gamoitane lamazad gamovidzaxet: {global_var} jer")

# print('from global scope', global_var)


def increment(number: float, increment_value: float = 1.0) -> float:
    """ 
    ეს ფუნქცია მიიღებს რიცხვს და გაზრდის მას +1 -ით ან 
    სასურველი რაოდენობით
    """
    print(type(increment_value))
    return number + increment_value


increment(5)
# increment(6, 2)
# increment(2.1)
my_num = 25

# for i in range(5):
#     my_num = increment(my_num)
#     print(my_num)

print(my_num)

def print_city(country: str = 'USA', city: str = 'Miami', population: int = 2000000):
    print(f'{country}, {city}, {population}')

# print_city()
# print_city("Georgia")
# print_city("Georgia", "tbilisi")
# print_city("Georgia", "tbilisi", 270000)


# unpacking
def my_function(*args, **kwargs):

    print(args[4])
    print(kwargs['name'])

# შეკრავს 
# my_function("Emil", "Tavil", 1, 2, 43, 45, 2, name="nick", age=25)


print('\n\n\n\n\n\n')

fib = [0, 1]

for i in range(1, 8):
    fib.append(fib[i] + fib[i - 1])

print(fib)


def fibb(n):
    if n <= 1:
        return n
    return fibb(n - 1) + fibb(n - 2)

fibb(50)