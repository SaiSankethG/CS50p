dict={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_amount=0
while True:
    try:
        item=input("Item:")
        for i in dict:
            if item==i:
                total_amount+=dict[item]
                print("Total: $")
                print(total_amount)
    except (EOFError , ValueError):
        print()
        break