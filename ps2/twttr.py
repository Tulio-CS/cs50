

def remove_vowels():
    msg = input("Input: ")
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for letter in msg:
        if letter in vowels:
            msg = msg.replace(letter,"")
    return msg


if __name__ == "__main__":
    print("Output:",remove_vowels())


