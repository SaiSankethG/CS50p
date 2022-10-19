def main():
    mass=int(input("m:"))
    joule=energy(mass)
    print("E:",joule , sep="")

def energy(mass):
    eng=mass*pow(300000000 , 2)
    return eng

main()