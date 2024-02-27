

def fuel():
    fraction = input("Fraction: ").split("/")
    try:
        x,y = int(fraction[0]),int(fraction[1])
        if not isinstance(x,int) or not isinstance(y,int):
            return fuel()
        if x > y:
            return fuel()
    except ValueError:
        return fuel()
    try:
        percentage = x/y
        if percentage >= 0.99:
            return "F"
        elif percentage <= 0.01:
            return "E"
        else:
            return "{}%".format(round(percentage * 100),1)
    except ZeroDivisionError:
        return fuel()


if __name__ == "__main__":
    print(fuel())
