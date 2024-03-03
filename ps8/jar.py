class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError
        self.__capacity = capacity
        self.__size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError

        else:
            self.size += n


    def withdraw(self, n):
         if n > self.size:
            raise ValueError
         else:
            self.size = self.size - n

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity <= 0 :
            raise ValueError
        else:
            self.__capacity = capacity

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,size):
        if size > self.capacity:
            raise ValueError
        else:
            self.__size = size



if __name__ == "__main__":
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)
