#how to make it so the decimal is at two
#f"${rent:.2f}"

while True:
    try:
        rent = float(input("What is your current rent cost?"))
        break
    except:
        print("It has to be a number, try again.")


while True:
    try:
        Utilities = float(input("What is your monthly utilities cost?"))
        break
    except:
        print("It has to be a number, try again.")


while True:
    try:
        groceries = float(input("What is your monthly groceries cost?"))
        break
    except:
        print(f"It has to be a number, try again.")


while True:
    try:
       transportation = float(input(f"What is your monthly transportation cost?"))
       break
    except:
        print(f"It has to be a number, try again.")


print(f"Your rent is {rent} and that is {rent/income*100}% of your monthly income ")







#everything is over income*100