def main():
    # amount_due=int(input("Amount Due:"))
    amount_due=50
    print("Amount Due:" , amount_due)
    while(amount_due>0 or amount_due<50):
        insert_coin=int(input("Insert Coin:"))
        total_insert=insert_coin
        amount_due-=insert_coin
        print("Amount Due:" , amount_due)
        if total_insert>50:
            change_owed=total_insert-50
            print("Changed Owed: " , change_owed)
        else:
            print("Changed Owed: 0")

main()
