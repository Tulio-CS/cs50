

def einstein(mass):
    c = 300000000 #m/s
    return mass * (c**2)


if __name__ == "__main__":
    mass = int(input("enter the mass in Kg: "))
    print(einstein(mass))
