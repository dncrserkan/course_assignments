class Jar():
    def __init__(self, capacity=12):
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity must be a positive number")

        self.current = 0

    
    def __str__(self):
        return "🍪" * self.current

    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Enter a positive number")
        elif self.current + amount > self.capacity:
            raise ValueError(f"There are too many cookies. \
                             Max amount you can add is \
                             {self.capacity - self.current}")
        else:
            self.current += amount
    

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Enter a positive number")
        elif amount > self.current:
            raise ValueError(f"In jar there is only {self.current} cookies")
        else:
            self.current -= amount


    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self.current


def main():
    jar = Jar()
    print(f"capacity: {str(jar.capacity)}")

    print(str(jar))
    
    jar.deposit(3)
    print(str(jar))

    jar.withdraw(1)
    print(str(jar))

    print(f"cookies in the jar: {jar.size}")


if __name__ == "__main__":
    main()