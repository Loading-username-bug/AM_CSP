# AM, Fixing Inputs

#when you want a spesific input

while True:
try:
        color = input("Tell me a color that is only one word:").lower().strip()
        elif " "color.isnumeric():
            print("umm thats not right go back to first grade and try again")
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

