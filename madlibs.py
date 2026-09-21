# AM, Mad libs no context

# Cleaning
# Cleaning is a very _______(adjective) thing to do. it keeps you from being ______(adgective) and helps you learn ______(adgective)_______(noun) habits. I clean often so my _____(noun) stays clean. thank you and remember to always _____(verp) cleaning.

adjective = input("Give me an adjective (Describes something).").strip().title()
adjective2 = input("Give me another adjective (Describes something).").strip().title()
adjective3 = input("Give me one last adjective (Describes something).").strip().title()
noun = input("Give me a noun (person, place, or thing).").strip().title()
noun2 = input("Give me another noun (person, place, or thing)").strip().title()
verb = input("Last but not least give me a verb (action)").strip().title()

print("Cleaning is a very" + " " + adjective +  " " + "thing to do. It keeps you from being" + " " + adjective2 + " " + "and helps you learn" + " " + adjective3 + " " + noun + " " + "habits. I clean often so my" + " " + noun2 + " " + "stays clean. Thank you and remember to always" + " " + verb + " " + "cleaning.")
