from datetime import date
import inflect
import sys
import operator

engine = inflect.engine()


def main():
    try:
        birth = input("Date of Birth: ")
        diff = operator.sub(date.today(), date.fromisoformat(birth))
        print(diff_to_min(diff.days))
    except ValueError:
        sys.exit(1)


def diff_to_min(diff):
    min = diff * 1440
    return "{} minutes".format(engine.number_to_words(min, andword="").capitalize())



if __name__ == "__main__":
    main()
