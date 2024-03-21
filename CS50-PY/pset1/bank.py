def main():
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(f"${amount}")


def value(text = " "):
    text = text.strip().lower()
    
    if len(text) == 0:
        return 0

    while not text[0].isalpha():
        text = text[1:]
    
    if text[:5] == "hello" or text[0] == " ":
        return 0
    elif text[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
