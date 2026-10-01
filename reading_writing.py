# AM, reading writing

with open('practice.txt', "r")as file:
    content = file.read()
    print(content)
    print(content.upper())
    word = content.find("Ainsley")
    length = len("Ainsley")
    print(content[word:word+length])

with open("practice.txt", "w") as file:
    file.write("Hello")