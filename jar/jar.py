import emoji

class Jar:
    def __init__(self, capacity=12):
        self._capacity=capacity
        if self._capacity<0:
            raise ValueError


    def __str__(self):
        return emoji.emojize(":cookie:")*self._capacity

    def deposit(self, n):
        

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

jar=Jar()
print(jar)