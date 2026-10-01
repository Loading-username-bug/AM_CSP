
#ceaser cypher = moves the item 4 times over. LaRose = PdVswi
#chr() converts it back to a letter
#take every letter make it number increase then back to letter. skip over all that not a letter
#ord=number chr=letter
e_d = input("Would you like to encript or decript something? If encript type E if decrypt type D")
message = input("Enter code")
shift = (int(input("Enter shift amount")))

if e_d == "E":
    result = ceaser_cipher

else:


#using range?

def ceaser_cipher(message,shift):
    for letter in message:
        if letter .isalpha():
            changed_number = ord(letter)
            if letter.isupper():
                start = ord("A")
            else:
                start = ord("a")

# postitions etc



