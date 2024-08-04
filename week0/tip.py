def main():
    dollars = dollars_to_float(input("How much was the meal: "))
    percent = percent_to_float(input("What percent would you like tip: "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    x = d.lstrip('$')
    return float(x)

def percent_to_float(p):
    y = p.strip('%')
    return float(y) / 100

main()