def checksum(card_number):
    total = 0
    card_number = list(reversed(card_number))
    for i in range(len(card_number)):
        if i % 2 == 0:
            total += int(card_number[i])
        else:
            temp = 2 * int(card_number[i])
            if temp > 9:
                total += (temp // 10) + (temp % 10)
            else:
                total += temp
    
    return total % 10 == 0


def main():
    while True:
        try:
            card_number = input("Number: ")
            if int(card_number):
                break
        except ValueError:
            continue

    length = len(card_number)
    AMEX =  ["34", "37"]
    MASTERCARD = ["51", "52", "53", "54", "55"]
    VISA = ["4"]

    if length == 15 and card_number[:2] in AMEX and checksum(card_number):
        print("AMEX")
    elif length == 16 and card_number[:2] in MASTERCARD and checksum(card_number):
        print("MASTERCARD")
    elif length in [13, 16] and card_number[0] in VISA and checksum(card_number):
        print("VISA")
    else:
        print("INVALID")

if __name__ == "__main__":
    main()
