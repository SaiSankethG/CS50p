dict={}
while True:
    try:
        name=input()
        value=1
        dict[value]=name
    except EOFError:
        print()
        break

