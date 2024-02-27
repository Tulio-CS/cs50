menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

def taqueria(val):
    try:
        order = input("Item: ").lower()
        print(f'Total:${val+menu[order]:.2f}')
        return taqueria(val+menu[order])
    except EOFError:
        return 0
    except KeyError:
        return taqueria(val)


if __name__ == "__main__":
    taqueria(0)

