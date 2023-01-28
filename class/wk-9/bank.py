# bal=0

# def main():
#     print("Balance:", bal)
#     deposit(100)
#     withdraw(50)
#     print("balance:", bal)

# def deposit(n):
#     global bal
#     bal+=n

# def withdraw(n):
#     global bal
#     bal-=n

class account:
    def __init__(self):
        self._bal=0

    @property
    def balance(self):
        return self._bal

    def deposit(self, n):
        self._bal+=n

    def withdraw(self, n):
        self._bal-=n

a=account()
print("Balance:" a.balance)

if __name__=="__main__":
    main()