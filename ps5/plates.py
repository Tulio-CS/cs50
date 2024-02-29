def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False
    elif plate[0] in "1234567890" or plate[1] in "1234567890":
        return False
    elif plate[len(plate)-2] in "1234567890" and plate[len(plate)-1] not in "1234567890":
        return False
    last_letter = plate[0]
    for letter in plate:
        if letter == "0" and last_letter not in "1234567890":
            return False
        elif letter not in "1234567890" and last_letter in "1234567890":
            return False
        else:
            last_letter = letter
    for punctuation in " ,.;:-_":
        if punctuation in plate:
            return False
    return True


main()

