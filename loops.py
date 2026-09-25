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


# like all data types saves variable (family)
# [] <- surrounds a list
# every item in list must be seperated by a comma
# every item in list must be correct data type
family = [" 'Damian", "mom", "papa," "pets"]
print(family[0])
print(family)
# add to the list
#item = input("What needs to be added to this list: ")
family.append("Grandmas")
family.insert(1,"Ainsley")
print(family)
# remove from the list
family.pop()
print(family)

# For loops
#(1,11) 1 = start point | 11 = end point does not include that number
# key word for for loop = for
#(1,11,2) 2 is the variable for the loop that keeps track of the current iteration of the loop
#  translation|for|each item|in|this list|
for number in range(1,11,2):
    print(number)

for family in familys:
    print(family + "Mugleston")
#family is the list name. next to it we put the brakets [index # of item I want] remember computers start counting at one.
#.appened(what is added to the list)
# "action happening"