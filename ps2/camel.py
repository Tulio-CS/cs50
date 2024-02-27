
def camel():
    camelCase = list(input("camelCase: "))
    snake_case = list()
    for letter in range(len(camelCase)):
        if camelCase[letter].isupper():
            snake_case.append("_")
        snake_case.append(camelCase[letter])
    snake_case = "".join(snake_case).lower()
    return snake_case



if __name__ == "__main__":
    print(camel())

