# AM, Fixing Inputs

#when you want a spesific input

while True:
    color = input("Tell me a color that is only one word:").lower().strip()

    if color.isnumeric():
            print("Umm thats not right go back to first grade and try again")
    elif " " in color:
            print("I said one word, learn to count.")
    else:
        break

print(f"I painted your walls {color}!")
# when you want a number
while True:
    try:
        age = int(input("how old are you: "))
        break
    except:
        print("That isn't a number")

print(f"wow you are {age} that is really old! Jeez grandma!")

