import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    c = re.findall(r"\b(um)\b",s,re.IGNORECASE)
    return len(c)



if __name__ == "__main__":
    main()
