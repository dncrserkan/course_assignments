NUM_ITEMS = 10


def main():
    global menu
    menu = []
    add_items(menu)

    print("Welcome to Burger Shack!")
    print("Choose  from the following menu to order. Press enter when done.\n")

    longest = max(map(len, [item['item'] for item in menu])) + 2    # Display better
    for i in range(NUM_ITEMS):
        print(f"{menu[i]['item']}".ljust(longest), f": ${menu[i]['price']:.2f}")
    print()

    total = 0
    while True:
        order = input("Enter a food item: ").strip().title()
        if len(order) == 0:
            print()
            break

        total += get_cost(order)
    
    print(f"Your total cost is: ${total:.2f}")


def add_items(menu):
    menu.append({"item": "Burger", "price": 9.5})
    menu.append({"item": "Vegan Burger", "price": 11})
    menu.append({"item": "Hot Dog", "price": 5})
    menu.append({"item": "Cheese Dog", "price": 7})
    menu.append({"item": "Fries", "price": 5})
    menu.append({"item": "Cheese Fries", "price": 6})
    menu.append({"item": "Cold Pressed Juice", "price": 7})
    menu.append({"item": "Cold Brew", "price": 3})
    menu.append({"item": "Water", "price": 2})
    menu.append({"item": "Soda", "price": 2})


def get_cost(item):
    global menu
    for i in range(NUM_ITEMS):
        if item == menu[i]["item"]:
            return menu[i]["price"]


if __name__ == "__main__":
    main()
