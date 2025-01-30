amount_due = 50
inserted_coin = 0

while inserted_coin < amount_due:
    x = amount_due - inserted_coin
    print(f"Amount Due: {x}")
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        inserted_coin += coin
y = inserted_coin - amount_due
print(f"Change Owed: {y}")
