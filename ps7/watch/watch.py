import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s)
    if link != None:
        return "https://youtu.be/{}".format(link.group(2))
    else:
        return None


if __name__ == "__main__":
    main()
