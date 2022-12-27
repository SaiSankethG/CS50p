import emoji

class Jar:
    def __init__(self, capacity=12 , size=0):
        self._capacity=capacity
        self._size=size
        if self._capacity<0:
            raise ValueError


    def __str__(self):
        return emoji.emojize(":cookie:")*self._capacity

    def deposit(self, n):
        self._size+=n
        if self._size>12:
            raise ValueError

    def withdraw(self, n):
        self._size-=n
        if self._size<0:
            raise ValueError


    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self._size

jar=Jar()
jar.deposit(13)
# print(jar)