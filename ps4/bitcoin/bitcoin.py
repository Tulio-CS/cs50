from sys import argv,exit
import requests



def get_n():
    if len(argv) == 2:
        try:
            if float(argv[1]):
                return argv[1]
        except ValueError:
            print("Command-line argument is not a number")
            exit(1)
    else:
        print("Missing command-line argument")
        exit(1)


def get_value(n):
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    usd = data["bpi"]["USD"]["rate_float"]
    result = float(usd) * float(n)
    print (f"${result:,.4f}")


def main():
    n = get_n()
    get_value(n)


main()


