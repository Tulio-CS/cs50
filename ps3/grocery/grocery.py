

def grocery(items = {}):
    try:
        item = input().upper()
        if item in items.keys():
            items[item] +=1
        else:
            items[item] = 1
        return grocery(items)
    except EOFError:
        for key,values in sorted(items.items()):
            print(values,key)
        return 0

if __name__ == "__main__":
    grocery()
