# AM, password

password = input("What is your password that needs to be tested?")

lenght = False
upper = False
lower = False
number = False
symbol = False

if len(password) >=8:
    print("true")
else:
    print("false")

if password.isupper():
    uppercase = True
else:
    uppercase = False

print(f"Has a uppercase letter: {uppercase}")

if password.islower():
    lowercase = True
else:
    lowercase = False

print(f"Has a lowercase letter: {lowercase}")
    
if password.isnumeric():
    number = True
else:
    number = False

print(f"Has a number: {number}")

if password in "$#!?@^%*&":
    symbol = True
else:
    symbol = False

print(f"Has a symbol: {symbol}")

strong = password is 