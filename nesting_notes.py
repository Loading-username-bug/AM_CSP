"""count = 0

while count <= 20:
    print(count)
    count += 2"""

"""for number in range(0,21,2):
    print(number)"""

#nesting: put a block of code inside another block of code

csp = ["Remy", "Alex", "Gabe", "Bliss", "Elsie", "Ivan", "Caydon", "Kaylee", "Levi", "Masen", "William", "Carrera", "Jacob", "Dara", "Ainsley", "Kristian" ]
if len(csp) > 0:
    for student in csp:
         print(f"Checking in {student}")
else:
    print("There is no one in this class.")

while True:
    username = input("What is your username: ").strip()
    password = input("What is your password: ")

    if username == "Ainsley23" and password == "password":
        print("Welcome to the program!")
        break
    else:
        print("Those credentials were incorrect")

