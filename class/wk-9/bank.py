global bal=0

def main():
    print("Balance:", bal)
    deposit(100)
    withdraw(50)
    print("balance:", bal)

def deposit(n):
    global bal
    bal+=n

def withdraw(n):
    global bal
    bal-=n

if __name__=="__main__":
    main()