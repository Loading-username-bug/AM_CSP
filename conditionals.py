# AM, 
 
 #CONDITIONALS
# A comnditional is a if you are _____ then go to _____. spesific

military_time = 1311

if military_time < 600:
    print("It's too early why are you awake")
elif military_time < 900:
    print("Good morning")
elif military_time < 1200:
    print("Good mornign! You should be at school.")
elif military_time < 1700:
    print("Good afternoon")
else:
    print("Good evening")
# ^
# |
#    what happens when nothing above is true    

# if is a keyword to sat the code
# |          Boolean statement. (statement that is either true or false)
# v       |
#         v

#if military_time > 1200:
    #print("It is the afternoon")

# a conditional is a block of code that checks to see if certain conditions are met


# COMPARISON OPERATIONS
# < less than
# > greater than
# >= greater than or equal to
# <= less than or equal
# == equal (python)
# === equal and same data type (not python)
# ! not (used with other operators)

#LOGICAL OPERATORS
#all of these are python only
# and | add info (both have to be met)
# or | add info (only one of those coditions has to be met)
# not | python only (when condition is not met) (use at begining of sentence)
# elif | checks another condition ONLY IF the other condition is false. (has to line up with the) 


# nesting is when you put somehting inside of its self |
#                                                      v
# nesting conditionals
day = "Saturday"
time = 900

if time > 900 and time < 1600:
    if day !="Saturday" or day != "Sunday":
        print("You should be at school")
    else:
        if time > 1200:
            print("Good afternoon")
        else:
            print("Good morning")
else:
    print("You are not required to go to school today")
