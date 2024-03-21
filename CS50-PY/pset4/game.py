import random


def main():
    level = get_number("Level: ")
    secret = random.randint(1, level)

    finished = False
    while not finished:
        guess = get_number("Guess: ")
        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            finished = True


def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
        except ValueError:
            pass


if __name__ == "__main__":
    main()
