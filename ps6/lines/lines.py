from sys import argv, exit


def is_valid():
    if len(argv) != 2:
        exit(1)
    elif argv[1].endswith(".py"):
        return True

def main():
    if is_valid():
        lines = 0
        try:
            with open(argv[1]) as file:
                for line in file:
                    if not line.lstrip().startswith("#") and not line.isspace():
                        lines += 1
        except FileNotFoundError:
            exit(1)
        return lines