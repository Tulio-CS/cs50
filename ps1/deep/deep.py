

def question():
    print("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer = input().lower()
    if "42" in answer or "forty two" in answer or "forty-two" in answer:
        return "yes"
    else:
        return "no"


if __name__ == "__main__":
    print(question())
