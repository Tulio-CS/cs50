

def convert(time):
    time = time.replace(" ","").split(":")
    return float(time[0]) + (float(time[1])/60)

def main():
    time = convert(input("What time is it: "))
    if time >= 7 and time <= 8:
        return("breakfast time")
    if time >= 12 and time <= 13:
        return("lunch time")
    if time >= 18 and time <= 19:
        return("dinner time")

if __name__ == "__main__":
    print(main())
