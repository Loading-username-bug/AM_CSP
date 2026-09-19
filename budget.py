# AM, Budgeting :)

monthly_income = float(input("What is your monthly income: $"))
monthly_utilities = float(input("What is your monthly utilities: $"))
monthly_rent_mortgage = float(input("What is your monthly rent/mortgage: $"))
monthly_groceries = float(input("What is your monthly utilities: $"))
monthly_transportation = float(input("What is your monthly transportation: $"))

savings = monthly_income / 10
net_expense = monthly_rent_mortgage + monthly_groceries + monthly_transportation + monthly_utilities
net_money = monthly_income - net_expense - savings

utilities_percent = round((monthly_utilities / monthly_income) * 100, 2)
rent_percent = round((monthly_rent_mortgage / monthly_income) * 100, 2)
groceries_percent = round((monthly_groceries / monthly_income) * 100, 2)
transportation_percent = round((monthly_transportation / monthly_income) * 100, 2)

print(f"Your rent is ${monthly_rent_mortgage} and that is {rent_percent}% of your income.")
print(f"Your rent is ${monthly_utilities} and that is {utilities_percent}% of your income.")
print(f"Your rent is ${monthly_groceries} and that is {groceries_percent}% of your income.")
print(f"Your rent is ${monthly_transportation} and that is {transportation_percent}% of your income.")
print(f"You should save ${savings} a month, that is 10 % of your income.")
print(f"You have ${net_money} of spending money each month! ")