def main():
    # amount_due=int(input("Amount Due:"))
    amount_due=50
    print("Amount Due: " , amount_due)
    while(amount_due>0 or amount_due<50):
        insert_coin=int(input("Insert Coin: "))
        total_insert=insert
        amount_due-=insert_coin
        print("Insert Coin:" , insert_coin)



