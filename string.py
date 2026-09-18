# String notes AM 
#any characters or symbols but must have quotation marks around it

#print(f '{name} told the class "I am very tired lol I can/'t stay awake" because she had gotten no sleep')
#instead of can't do can/'t. the slash means that it tells the computer to remove the character that comes riht after it.
#escape char lets the program ignore the next character in the string

#concatenation => add twon string together

last_name = 'mugleston'
first_name = 'ainsley'
name = first_name = " " + last_name

#'lkfjaf' "aelijfalf" surround with quotes
#first_name + " " Last_name   puts two strings together
#{ ;ldjfw} means taking a break form the string
# f-string = formatting string -> name = f"{first_name} {last_name}""
print(f'{name} told the class "you can\'t drive my car"')

user = input("Please tell me your name:\n").strip().title()

print(f"New user recognized\nWelcome {user}")

sentence = "The quick brown fox jumped over the lazy dog."

print(sentence)
print(sentence.replace("dog", "cat"))
print(f"The sentence is {len(sentence)} characters long")