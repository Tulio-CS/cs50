from validators import email


def main():
    print(validate(input("What's your email asress? ")))

def validate(s):
    if email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
