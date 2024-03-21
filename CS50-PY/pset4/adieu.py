import inflect


p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break


text = "Adeiu, adeiu, to "
text += p.join(names)
print(text)
