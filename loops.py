# AM, Loops Notes
import random
# loop = code that will repeate over and over again
# infinite loop = writte so the loop will never end
# itorater = keping track of how many times you have done it
# while is the key word that starts a while loops
# while loop = a loop that will go until there is something new thayt will cause it to end
# += increases variable & resets the value
# continue = stops the iteration and restarts the whole thing

# 1 start point (1)
count = 1

# 2 stop point (count <+ 10)

while count <= 10:
    print(count)
# 3 iterator (count += 1) 
    count += 1

goose = random.randint(1,11)
ducks = 1

while True:
    print("duck")
    if ducks == goose:
        break
    ducks += 1
print("GOOSE!")


# like all data types saves variable (siblings)
# [] <- surrounds a list
# every item in list must be seperated by a comma
# every item in list must be correct data type
siblings = ["Damian"]