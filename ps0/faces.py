
def convert(msg):
    msg = msg.replace(":)","🙂")
    msg = msg.replace(":(","🙁")
    return msg



def main():
    msg = input()
    print(convert(msg))



if __name__ == "__main__":
    main()


