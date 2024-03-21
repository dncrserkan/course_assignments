def main():
    while True:
        try:
            minimum = int(input("Minimum: "))
            maximum = int(input("Maximum: "))
            if minimum >= 1 and maximum > minimum:
                break
        except ValueError:
            continue        
    
    for i in range(minimum, maximum):
        if prime_v3(i):
            print(i)


def prime_v1(number):
    """ Return True if 'number' is prime, False otherwise. """
    if number == 1:
        return False    # 1 is not prime
    
    for d in range(2, number):
        if number % d == 0:
            return False

    return True


def prime_v2(number):
    """ Return True if 'number' is prime, False otherwise. """
    if number == 1:
        return False    # 1 is not prime

    max_divisor = int(number ** 0.5)
    for d in range(2, 1 + max_divisor):
        if number % d == 0:
            return False
    
    return True


def prime_v3(number):
    """ Return True if 'number' is prime, False otherwise. """
    if number == 1:
        return False    # 1 is not prime
    
    if number != 2 and (number % 2) == 0:
        return False
    
    max_divisor = int(number ** 0.5)
    for d in range(3, max_divisor + 1, 2):
        if number % d == 0:
            return False
    
    return True


if __name__ == "__main__":
    main()
