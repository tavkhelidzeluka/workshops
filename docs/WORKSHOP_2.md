
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
