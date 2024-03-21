import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s=""):
    # if there is lenght is not in acceptable range
    minimum, maximum = 2, 6
    if not minimum <= len(s) <= maximum:
        return False
    
    # if there is any nonalphabetic character in the first two places
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
  
    not_allowed = string.punctuation + " "  # Not acceptable characters
    flag = False                            # Flag will be used for numeric characters
    for i, char in enumerate(s):

        if char in not_allowed:
            return False

        if char.isnumeric() and not flag: 
            flag = True             # No need to search further numeric values
            
            if char == "0":
                return False        
            
            for any_char in s[i+1:]:
                if any_char.isalpha():
                    return False

    return True


if __name__ == "__main__":
    main()
