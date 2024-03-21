while True:
    try:
        dollars = float(input("Change owed: "))
        if dollars > 0:
            break
    except ValueError:
        continue

cents = dollars * 100

quarters = cents // 25
cents -= quarters * 25

dimes = cents // 10
cents -= dimes * 10

nickels = cents // 5
cents -= nickels * 5

pennies = cents // 1

total = int(quarters + dimes + nickels + pennies)
print(total)
