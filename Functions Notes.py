# AM, Notes Functions
#didn't finish
#round()
#len()
#print()
#peramaters are variables inside of the function 
#use a function to get rid of repetetive code, makes code easier to red, better orginized
# when to use, if it would be easier to understand seperate, if it is a long prosses that should be done independantly, and if it is a;sp 

def stupid_proof(money):
    while True:
        try:
            temp = float(input(f"What is your monthly {money}:"))
            return temp
        except:
            print("That is not a number :(")



income = float(input("What is your monthly income"))
rent = float(input("What is your monthly rent"))
utilities = float(input("What is your monthly utilities"))
transportation = float(input("What is your monthly transportation"))
groceries = float(input("What is your monthly groceries"))
#variables go first
# functoins always go second
#def is how to make or define a function

def calc_percent(bill, income):
    return round(bill/income * 100)

save

print(f"Your monthly rent is ${rent} which is {calc_percent(rent,income)}%of your income ")
#calc_percent names the functoin
#puts the info into the function call/whatever she calls the function
#{calc_percent(utilities,income)} is the function call
print(f"Your monthly utilities is ${utilities} which is {calc_percent(utilities,income)}%of your income ")
print(f"Your monthly transportation is ${transportation} which is {calc_percent(transportation,income)}%of your income ")
print(f"Your monthly groceries is ${groceries} which is {calc_percent(groceries,income)}%of your income ")
print(f"You should save ${round(income*.1, 2)} which is 10% of your income")
print(f"That means you have {income-rent-utilities-transportation-groceries-(income*.1)}")
print(f"You should save is ${save} which is 10% of your income")

income = stupid_proof(income)
rent = stupid_proof(rent)
utilities = stupid_proof(utilities)
transportation = stupid_proof(transportation)
groceries = stupid_proof(groceries)