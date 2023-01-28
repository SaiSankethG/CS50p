class Cat:
    MEOW=10

    def meow(self):
        for _ in range(self.MEOW):
            print("Meow")

Cat().meow()