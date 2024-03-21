class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n=0):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be positive interger")
        elif self._size + n > self._capacity: 
            raise ValueError("too many cookies")
        self.size = self._size + n


    def withdraw(self, n=0):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be positive integer")
        elif n < 0 or n > self._size:
            raise ValueError("n is not positive or greater than size")
        self.size = self._size - n
    

    @property
    def capacity(self):
        return self._capacity 
    

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be positive integer")
        self._capacity = capacity


    @property
    def size(self):
        return self._size 

 
    @size.setter
    def size(self, old=0, n=0):
        self._size = old + n
