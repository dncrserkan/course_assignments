def main():
    while True:
        try:
            bill_amount = float(input("Bill before tax an tip: "))
            tax_percent = float(input("Sale Tax Percent: "))
            tip_percent = int(input("Tip percent: "))
            break
        except ValueError:
            continue
        

    print("You will owe ${:.2f} each!".format(half(bill_amount, tax_percent, tip_percent)))


def half(bill, tax, tip):
    total = bill
    total += total * tax / 100
    total += total * tip / 100
    each = total / 2
    return each


if __name__ == "__main__":
    main()