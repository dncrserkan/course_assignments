def main():
    camel = input("camelCase: ")
    snake = camel_to_snake(camel)
    print("snake_case:", snake)


def camel_to_snake(name):
    new_name = ""
    for char in name:
        if char.isupper():
            new_name += "_" + char.lower()
        else:
            new_name += char
    return new_name


if __name__ == "__main__":
    main()
