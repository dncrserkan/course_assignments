def main():
    card_number = get_card_number()
    digits = turn_number_to_list(card_number)
    checksum = calculate_sum(digits)
    is_it_valid_card(checksum, card_number)


def get_card_number():
    ''' this function ask the user for a card number and check it,
        if it is not a positive number then ask again and again 
    return type -> string'''

    while True:
        try:
            temp = input("What is your credit card number? ")
            if int(temp) > 0:   # check for is input a positive number
                return temp
        except ValueError:
            continue


def turn_number_to_list(card_number):
    ''' this function takes the card number and separate it to digits as integer 
    return type -> list of integers '''
    temp = []
    for i in range(len(card_number)):
        temp.append(int(card_number[i]))
    return temp

    
def calculate_sum(digits):
    """ this function calculate the sum of digits
    return type -> integer """
    # Create a reverse list for simple stepping
    digits.reverse()

    # Arrange items with multiplication
    for i in range(len(digits)):
        if i % 2 == 0:
            continue
        else:
            digits[i] *= 2
    
    # Calculate the sum and check if any value has two digits 
    total = 0
    for number in digits:
        if number >= 10:
            for j in str(number):
                total += int(j)
        else:
            total += number

    return total


def is_it_valid_card(checksum, card_number):
    """ this function is check the sum and card number according to the specifications 
    return type -> nothing """
    number_of_digits = len(card_number)
    if checksum % 10 == 0:
        if number_of_digits in [13, 16] and card_number[0] == "4":
            print("VISA")
        elif number_of_digits == 15 and card_number[:2] in ["34", "37"]:
            print("AMEX")
        elif number_of_digits == 16 and card_number[:2] in ["51", "52", "53", "54", "55"]:
            print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
