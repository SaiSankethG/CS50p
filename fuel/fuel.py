def main():
    while True:
        try:
            x, y =int(input("Fraction:")).split()
            z=x/y
        except (ValueError , ZeroDivisionError):
            continue
        else:
            break

    


main()

