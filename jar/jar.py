import emoji

class Jar:
    def __init__(self, capacity=12 , size=0):
        self._capacity=capacity
        self._size=size
        if self.capacity<0:
            raise ValueError

    def __str__(self):
        return emoji.emojize(":cookie:")*self._size

    def deposit(self, n):
        if self.size+n>12:
            raise ValueError
        if n>self.capacity:
            raise ValueError
        self._size+=n

    def withdraw(self, n):
        if self._size-n<0:
            raise ValueError("Less than Zero")
        self._size-=n

    @property
    def capacity(self):
        # print(self._capacity)
        return self._capacity

    @property
    def size(self):
        return self._size


jar=Jar()
jar.deposit(12)
# jar.withdraw(1)
# jar.capacity()
print(jar)
