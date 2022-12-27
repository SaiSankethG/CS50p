import emoji

class Jar:
    def __init__(self, capacity=12):
        self._capacity=capacity
        if self._capacity<0:
            raise ValueError


    def __str__(self):
        return emoji.emojize(":cookie:")*self._capacity

    def deposit(self, n):
        self.capacity+=n
        if self.capacity>12:
            raise ValueError

    def withdraw(self, n):
        self.capacity-=n
        if self.capacity<0:
            raise ValueError


    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

jar=Jar()
print(jar)