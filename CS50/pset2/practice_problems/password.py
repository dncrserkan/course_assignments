import string


password = input("Enter your pasword: ")

flag_upper = False
flag_lower = False
flag_numeric = False
flag_punc = False

for char in password:

    if char.isupper():
        flag_upper = True
        continue
    elif char.islower():
        flag_lower = True
        continue
    elif char.isnumeric():
        flag_numeric = True
        continue
    elif char in string.punctuation:
        flag_punc = True
        continue

if all([flag_upper, flag_lower, flag_numeric, flag_punc]):
    print("Your password is valid!")
else:
    print("Your password needs at least one uppercase letter, lowercase letter, number and symbol!")