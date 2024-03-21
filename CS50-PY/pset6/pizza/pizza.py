import sys
import csv
from tabulate import tabulate


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

choice = sys.argv[1]
if choice[-4:] != ".csv":
    sys.exit("Not a CSV file")

menu = []
name = choice[:-4].title() + " Pizza"
try:
    with open(choice) as file:
        reader = csv.DictReader(file, fieldnames=[name, "Small", "Large"])
        for row in reader:
            menu.append(row)
        del menu[0]     # or tabulate headers can be changed with "firstrow"
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(menu, headers="keys", tablefmt="grid"))
