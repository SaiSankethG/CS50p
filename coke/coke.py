def main():
    # amount_due=int(input("Amount Due:"))
    amount_due=50
    while amount_due>0:
        print("Amount Due:" , amount_due)
        insert_coin=int(input("Insert Coin: "))
        if insert_coin in[25 , 10 , 5]:
                amount_due-=insert_coin
    change_owed=abs(amount_due)
    print("Change Owed:" , change_owed)

main()
