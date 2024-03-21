from validator_collection import validators, errors


mail = input("What's your email address? ")

try:
    if validators.email(mail, allow_empty = True):
        print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
