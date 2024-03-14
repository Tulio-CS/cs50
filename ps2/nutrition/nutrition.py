

def calories():
    food = input("Item: ").lower()
    poster = {"apple":130,"avocado":50,"kiwifruit":90,"pear":100,"sweet cherries":100}
    if food in poster.keys():
        return poster[food]


if __name__ == "__main__":
    val = calories()
    if val:
        print("Calories:",val)
