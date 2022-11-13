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
        item=input("Item: ").title()
        if item in dict:
            total_amount+=dict[item]
            print("Total: $" ,end="")
            print(f"{total_amount:.2f}")
    except (EOFError , ValueError):
        print()
        break