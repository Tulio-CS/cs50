

def interpreter():
    operation = input("Expression: ").split(" ")
    if operation[1] == "+":
        return round(float(operation[0]) + float(operation[2]),1)
    if operation[1] == "-":
        return round(float(operation[0]) - float(operation[2]),1)
    if operation[1] == "*":
        return round(float(operation[0]) * float(operation[2]),1)
    if operation[1] == "/":
        return round(float(operation[0]) / float(operation[2]),1)


if __name__ == "__main__":
    print(interpreter())
