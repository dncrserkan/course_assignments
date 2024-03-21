val = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

match val.lower():
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
