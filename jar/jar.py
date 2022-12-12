class Jar:
    def __init__(self, capacity=12)
        self.capacity=capacity:
        if self.capacity<0:
            raise ValueError


    def __str__(self):
        print(🍪*4)

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

print(Jar())