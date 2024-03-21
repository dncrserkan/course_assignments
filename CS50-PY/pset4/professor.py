import random


def main():
    level = get_level()
    LIMIT = 10
    score = 0
    counter = 0
    life_counter = 3
    asking_again = False    # In case a wrong answer, need to ask same question again
    while counter < LIMIT:
        if not asking_again:
            X, Y, CORRECT = generate_integer(level)

        print(f"{X} + {Y} = ", end="")
        answer = get_answer()

        if answer == CORRECT:
            score += 1
            counter += 1
            life_counter = 3
            asking_again = False
        else:
            life_counter -= 1
            if life_counter == 0:
                counter += 1
                life_counter = 3
                asking_again = False
                print("EEE")
                print(f"{X} + {Y} = {CORRECT}")
            else:
                print("EEE")
                asking_again = True
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                return level
        except ValueError:
            pass


def generate_integer(level):
    def generate():
        return random.randint(1, 899)
    
    def fit_range(number, level):
        match level:
            case 1:
                return number % 10
            case 2:
                return number % 90 + 10     # To prevent one digit numbers
            case 3:
                return number % 900 + 100   # To prevent one and two digits numbers
    
    X = fit_range(generate(), level)
    Y = fit_range(generate(), level)
    return (X, Y, X + Y)


def get_answer():
    try:
        ans = float(input())
        if ans % 1 != 0:
            raise ValueError
        return int(ans)
    except ValueError:
        return None


if __name__ == "__main__":
    main()
