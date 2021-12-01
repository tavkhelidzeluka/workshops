# Python

<details>
    <summary>დავალებები</summary>

[დავალება 1](https://forms.gle/GF8Z63eRmKc2QfUe8)

</details>

<details>
    <summary>Workshop 1</summary>

*I/O (Input/Output)*
```python
# ტერმინალში (CLI, CMD, Console) გამოტანა:
print("Hello World!")

# ტერმინალიდან ინფორმაციის მიღება
input("Enter any value: ")
```

*Variables*
```python
# მინიჭების ოპერატორი (=)
"""
    იმისათვის, რომ ცვლადი შევქმნათ გვჭირდება მინიჭების
    ოპერატორი =

    ცვლადის_სახელი: მონაცემთა ტიპი = მნიშვნელობა
"""
my_var: int = 4

```

*მონაცემთა ტიპები*
- int (Integer)
    
    ```python
    # მათემატიკური აღნიშვნა - Z
    """
        მნიშვნელობათა სიმრავლე (მათემატიკაში)
        (-∞, ..., -1, 0, 1, ..., ∞)
    """

    # მაქსიმალური მნიშვნელობა
    """
        პითონში მაქსიმალური რიცხვი დამოკიდებულია 
        თქვენს კომპიუტერზე
    """
    import sys

    print(sys.maxsize)

    # initialization (ცვალდის შექმნა)
    my_int: int = 5

    """
        (: int) არ არის აუცილებელი, მაგრამ
        PEP 8 stantard -ი გვეუბნება, რომ გამოვიყენოთ
    """
    ```
- str (String)

    ```python
    """
        მონაცემთა ტიპი, რომლის დანიშნულებაა
        შეინახოს ტექსტური მონაცემი - სტრიქონი (სიტყვა),
        რომელიც კომპიუტერში წარმოდგენილია 
        ასოების (character) მიმდევრობით.
    """
    # initialization (ცვლადის შექმნა)
    my_string_1: str = "I'm string"
    my_string_2: str = 'I\'m also a string'
    my_string_3: str = '''I\'m also a string'''
    # my_string_4: str = """I\'m also a string"""

    # concatenation (სტრინგების გადაბმა/მიმატება)
    my_string_1 + my_string_2

    # f strings
    special_string: str = f'{my_string_1}, but I am special!'

    """
        f -სტრინგები, რომელიც ახალი დამატებაა
        პითონში და გვეხმარება, ძალიან მარტივად
        ჩავწეროთ ჩვენი ცვალდები სტრინგში
    """

    ```

- bool (Boolean)
    ```python
    """
        მონაცემთა ტიპი, რომელსაც მხოლოდ 2 მნიშვნელობის
        მიღება შეუძლია (True ან False).

        "გამონათქვამი შეიძლება ან მცდარი იყოს ან ჭეშმარიტი"
    """

    # initialization (ცვლადის შექმნა)
    is_programmer: bool = True
    ```

- float (Fractions)
    ```python
    """
        მონაცემთა ტიპი, რომელიც არის წილადი რიცხვები

        მათემატიკური აღნიშვნა - Q
        მნიშვნელობათა სიმრავლე
        (-∞, ..., -1/2, -1/3, 0, 1, ..., ∞)

    """
    PI: float = 3.14
    ```

*Type hinting (ტიპების მითითება)*
```python
"""
    ცვლადის შემდგომ ორწერტილის (:) შემდეგ 
    მომავალი keywrod-ი განსაზღვრავს მის მნიშვნელობას,
    ეს არის მხოლოდ დეველოპერისთვის და იმისათვის, 
    რომ ეედიტორი დაგეხმაროთ
"""
my_int: int = -5
my_string: str = "Hello"
my_bool: bool = False
my_float: float = 3.14
```

*Type Casting (ტიპების შეცვლა)*
```python
"""
    მონაცემთა ერთი ტიპიდან მეორეში გადასვლას
    type casting -ი ეწოდება (გადაქასთვა)
"""

what_character_is_this = 65
print(chr(what_character_is_this)) # პითონში char - სტრინგია
# უბრალოდ chr ფუნქციას გადაყავს int-ი ASCII-ში

name: str = "John"
last_name: str = "Doe"
age: int = 54

print(name + last_name + str(age))
print(name, last_name, age) # აქ გადაქასთვა ხდება ჩვენგან დამალულად

"""
    რა მოხდება მთელი რიცხვი, რომ bool -ში გადავქასთო?
"""
```


*Conditional Statements (if/else)*
```python
"""
    თუ (პირობა):
        აქ დაწერილი კოდი გააკეთე
    თუ არადა:
        აქ დაწერილი კოდი გააკეთ
"""

if (5 > 1):
    """აქ შემოვა?"""
else:
    """თუ აქ?"""

"""
    ფრჩხილები -> () არ არის აუცილებელი!

    4 სფეისით (1 ტაბით) შეწეულ კოდს
    ეწოდება code block (ტანი),

    if -ის შემთხვევაში ორწერტილის(:) შემდგომ
    შეწეულ ნაწილს რა ეწოდება?
"""
```

*Basic syntax Errors*

```python
# varibale naming (რა არ შეგიძლიათ დაარქვათ ცვლადს)

int = 5 # შედომაა რადგან ეს keyword რეზერვირებულია

# კიდევ მსგავსი რა შეცდომები წარმოგიდგენიათ?

##################

1_variable = 3 # ცვლადის სახელი უნდა იწყებოდეს ასოთი

"""
    (a - z) (A - Z)
    ამ სიმრავლიდან ნებისმიერი ასოთი შეგიძლიათ დაიწყოთ
    ცვლადის დასახელება 
    (თუ შესაძლებელია, მხოლოდ ASCII გამოიყენეთ!)
"""
my1var = 3 #  შესაძლებელი მაგრამ არა რეკომენდებული


###################

"""
    აკონტროლეთ ინდენტაცია (Indentation), ანუ
    რამდენად შეწეული კოდი, რადგან code block
    განისაზღვრება შეწევით (1 tab/4 space).

    არ გამოიყენოთ ორივე, ან space ან tab!
"""
 variable = 5 #  შეცდომა
variable = 5 #  სწორი

    variable = 5 #  შეცდომა

if variable > 4:
        print("hehe shampoo!") # სწორია თუ არა?
else:
    print("which's right? me or ↑?")
    

if variable > 0:
    print("variable is positive")
    else:
        print("Am I correctly possitioned?")
```

</details>


<details>
<summary>Workshop 2</summary>

*მეტი conditional statement-ების შესახებ*
```python

age = 20
if age > 50:
    print("elder")
if age > 30:
    print("adult")
if age > 18:
    print("young adult")
else:
    print("young")

"""
    მინიმუმ რამდენი შემოწმება მოხდება? (best case)
    და მაქსიმუმ რამდენი შემოწმება მოხდება? (worst case)
"""

"""
    if/else chaining

    თუ (პირობა 1):
        პირობა 1 შესრულდა შემოდი აქ
    თუ არა და (პირობა 2):
        პირობა 2 შესრულდა შემოდი აქ
    თუ არა და (პირობა 3):
        პირობა 3 შესრულდა შემოდი აქ
    ყველა დანარჩენი შემთხვევა:
        შემოდი აქ
"""

age = 20
if age > 50:
    print("elder")
elif age > 30:
    print("adult")
elif age > 18:
    print("young adult")
else:
    print("young")

"""
    მინიმუმ რამდენი შემოწმება მოხდება? (best case)
    და მაქსიმუმ რამდენი შემოწმება მოხდება? (worst case)
"""

"""
    ახალი keywords - and, or
    ფრჩხილებში ჩასმულ ნაწილს (ფრჩხილები არაა აუცილებელი!)
    ეწოდება statement-ი (პირობა), თუ ის ჭეშმარიტია, მაშინ
    მისი evaluation -ი მოხდება და ან True იქნება ან False
"""

name = "nick"
age = 18
if (age == 18 and name == "nick"):
    print("do something")
elif age < 18 or name == "Erick":
    print("do something")

```

*Data structures*
```python
"""
    მონაცემთა სტრუქტურები - list, tuple, dict, set
    მათი დანიშნულებაა ობიექტების გაერთიანება, როდესაც ბევრი
    მსგავსი ცვლადი გვჭირდება.

    list - სხვა ენებში (array), muttable დინამიური მონაცემთა ტიპი.
    tuple 0
"""

# ჩვენ აქამდე შევეხეთ ერთ-ერთ მონაცემთა ტიპს
# რომელსაც მასივი (რაღაც ერთობლიობა) ეწოდება 
# ეს იყო str, რატომ შეიძლება იყოს str მასივი?
```

</details>