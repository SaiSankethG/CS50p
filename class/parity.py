# x=int(input("Whats is x?"))

# if x%2==0:
#     print("X is even")
# else
#     print("X is odd")

def main():
    x=int(input("Whats is X?"))
    if is_even(x):
        print("Even")
    else:
        print("odd")

def is_even(y):
    return y%2==0

main()