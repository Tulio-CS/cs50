from sys import argv,exit
from PIL import Image,ImageOps

def is_valid():
    if len(argv) != 3:
        exit(1)
    elif argv[1].endswith(".png") or argv[1].endswith(".jpeg") or argv[1].endswith(".jpg"):
        if argv[2].endswith(".png") or argv[2].endswith(".jpeg") or argv[2].endswith(".jpg"):
            if argv[1][-3:] == argv[2][-3:] or argv[1][-4:] == argv[2][-4:]:
                return True
            else:
                exit(1)
        else:
            exit(1)
    else:
        exit(1)


def main():
    if is_valid():
        try:
            with Image.open(argv[1]) as image:
                shirt = Image.open("shirt.png")
                size = shirt.size
                image = ImageOps.fit(image,size)
                image.paste(shirt,shirt)
                image.save(argv[2])
        except Exception:
            exit(1)


if __name__ == "__main__":
    main()


