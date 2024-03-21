def main():
    total = 0
    price = 50

    while total < price:
        print(f"Amount Due: {price - total}")
        total += get_coin()

    change = total - price
    print(f"Change Owed: {change}")


def get_coin():
    coins = [25, 10, 5]     # Acceptable coins
    temp = int(input("Insert Coin: "))
    if temp in coins:
        return temp
    return 0


if __name__ == "__main__":
    main()
