# AM, password

password = input("What is your password that needs to be tested?")

lenght = False
upper = False
lower = False
number = False
symbol = False

symbols = "$#!?@^%*&"

strong = 0
medium = 0
weak = 0

if len(password) >=8:
    length = True


for letter in password:
    if letter.isupper():
        uppercase = True

    if letter.islower():
        lowercase = True

    if letter.isnumeric():
        number = True

    if letter in symbols:
        symbol = True

score == 0
if length:
    score = score + 1
if uppercase True:
    score = score + 1
if lowercase True:
    score = score + 1
if number True:
    score = score + 1
if symbol True:
    score = score + 1


print(f"Has a uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")
