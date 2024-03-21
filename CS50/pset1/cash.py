def get_cents():
    while True:
        try:
            temp = int(input("How many cents the customer is owed? "))
            if temp >= 0:
                return temp
        except ValueError:
            continue


def calculate_quarters(cents):
    return cents // 25


def calculate_dimes(cents):
    return cents // 10


def calculate_nickels(cents):
    return cents // 5


def calculate_pennies(cents):
    return cents // 1


# Ask how many cents the customer is owed
cents = get_cents()

# Calculate the number of coins to give the customer
quarters = calculate_quarters(cents)
cents = cents - quarters * 25

dimes = calculate_dimes(cents)
cents = cents - dimes * 10

nickels = calculate_nickels(cents)
cents = cents - nickels * 5

pennies = calculate_pennies(cents)
cents = cents - pennies * 1

# Sum coins
coins = quarters + dimes + nickels + pennies

# Print total number of coins to give the customer
print(f"Total coins: {coins}")
# print(f"Quarters: {quarters} \t Dimes: {dimes} \t Nickels: {nickels} \t Pennies: {pennies}")
