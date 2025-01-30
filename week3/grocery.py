grocery = {}

while True:
    try:
        item = input("").strip().lower()
        grocery[item] += 1
    except KeyError:
        grocery[item] = 1
    except EOFError:
        sorted_grocery = sorted(grocery.items())
        for key, value in sorted_grocery:
            print(f"{value} {key}")
        break