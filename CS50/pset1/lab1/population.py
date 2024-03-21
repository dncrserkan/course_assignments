import sys


# Get input for current llamas
while True:
    try:
        current_llamas = int(input("How many llamas: "))
        if current_llamas >= 9:
            break
    except ValueError:
        print("It must be an integer")
        sys.exit(1)

# Get input for wanted llamas
while True:
    try:
        wanted_population = int(input("How many llamas you wanted: "))
        if wanted_population > current_llamas:
            break
    except ValueError:
        print("It must be an integer which is grater than current llamas")
        sys.exit(1)

# Make calculations for time
passed_years = 0

while current_llamas < wanted_population:
    gain_llamas = current_llamas // 3
    lose_llamas = current_llamas // 4
    current_llamas = current_llamas + gain_llamas - lose_llamas
    passed_years += 1

print(f"Years: {passed_years}")
