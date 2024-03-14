import emoji

def main():
    text = input("Input: ")
    return emoji.emojize("Output: {}".format(text),language = "alias")


if __name__ == "__main__":
    print(main())

