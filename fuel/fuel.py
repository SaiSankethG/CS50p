def main():
    while True:
        try:
            x, y =int(input("Fraction:")).split()
            print(f"x is {x} , y is {y}")
        except (ValueError , ZeroDivisionError):
            continue
        else:
            break




main()

