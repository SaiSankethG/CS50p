import emoji

class Jar:
    def __init__(self, capacity=12 , size=0):
        self._capacity=capacity
        self.size=size
        if self._capacity<0:
            raise ValueError


    def __str__(self):
        return emoji.emojize(":cookie:")*self._capacity

    def deposit(self, n):
        self.size+=n
        if self.size>12:
            raise ValueError

    def withdraw(self, n):
        self.size-=n
        if self.size<0:
            raise ValueError


    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size

jar=Jar()
print(jar)