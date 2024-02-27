

def coke_machine():
    coke_value = 50
    amount_inserted = 0
    while amount_inserted < coke_value:
        print("Amount Due:", coke_value - amount_inserted)
        coin = int(input("Insert Coin: "))
        if coin in [5,10,25]:
            amount_inserted += coin
    change_owned = amount_inserted - coke_value
    print("Change Owed:", change_owned)

if __name__ == "__main__":
    print(coke_machine())
