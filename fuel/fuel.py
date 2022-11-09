while True:
    try:
        x, y =int(input("Fraction:")).split("/")
    except(ValueError , ZeroDivisionError):
        continue


