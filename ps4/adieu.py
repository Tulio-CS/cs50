import inflect

def main(names=[]):
    try:
        name = input("Name: ")
        names.append(name)
        return main(names)
    except EOFError:
        return "Adieu, adieu, to {}".format(inflect.engine().join(names))



if __name__ == "__main__":
    print(main())



