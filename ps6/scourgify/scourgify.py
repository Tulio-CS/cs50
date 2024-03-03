from csv import DictReader,DictWriter
from sys import argv,exit


def get_path():
    if len(argv) != 3:
        exit(1)
    else:
        if argv[1].endswith(".csv") and argv[2].endswith(".csv"):
            print(argv)
            return True
        else:
            exit(1)


def main():
    if get_path():
        try:
            students = []
            with open(argv[1],"r") as before, open(argv[2],"w") as after:
                reader = DictReader(before)
                writer = DictWriter(after, fieldnames=['first', 'last', 'house'])
                writer.writeheader()
                for row in reader:
                    last,first  = row["name"].split(", ")
                    writer.writerow({"first":first,"last":last,"house":row["house"]})
        except FileNotFoundError:
            exit(1)

if __name__ == "__main__":
    main()
