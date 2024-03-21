import re
import sys
import inflect
from datetime import date


def main():
    year, month, day = validate(input("Date of Birth: "))
    print(calculate(date(year, month, day), date.today()))


def calculate(birthday, today):
    age = (today - birthday).days
    if age < 0:
        sys.exit("Invalid date")    # born in future
    age_in_minutes= age * 24 * 60
    
    p = inflect.engine()
    return p.number_to_words(age_in_minutes, andword=",").capitalize()


def validate(text=""):
    expression = r"^(\d{4})-(\d{1,2})-(\d{1,2})$"
    if matches := re.search(expression, text):
        year, month, day = matches.groups()
        try:
            year, month, day = int(year), int(month), int(day)
            if (not 0 < month <= 12 ) or (not 0 < day <= 31):
                sys.exit("Invalid date") # month or day not in range
            return (year, month, day)
        except ValueError:
            sys.exit("Invalid date") # not integer
    else:
        sys.exit("Invalid date") # wrong format


if __name__ == "__main__":
    main()
