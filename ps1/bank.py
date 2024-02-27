

def greeting():
    msg = input("Greeting: ").lower()
    if "hello" in msg:
        return "$0"
    elif msg[0] == "h":
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    print(greeting())
