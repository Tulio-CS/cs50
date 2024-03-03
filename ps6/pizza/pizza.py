from sys import argv,exit
from tabulate import tabulate
from csv import DictReader


def get_path():
    if len(argv) != 2:
        exit(1)
    else:
        if argv[1].endswith(".csv"):
            return True
        else:
            exit(1)


def main():
    if get_path():
        with open(argv[1],"r") as file:
            csv = DictReader(file)
            return (tabulate(csv,tablefmt="grid",headers="keys"))


if __name__ == "__main__":
    print(main())
