menu = {
    "Baja Taco"       : 4.25,
    "Burrito"         : 7.50,
    "Bowl"            : 8.50,
    "Nachos"          : 11.0,
    "Quesadilla"      : 8.50,
    "Super Burrito"   : 8.50,
    "Super Quesadilla": 9.50,
    "Taco"            : 3.00,
    "Tortilla Salad"  : 8.00,
}
price = 0
while True:
    try:
        choice = input("Item: ").title()
    except EOFError:
        print(f"Total: {round(price, 2)} ", end='\n')
        break
    else:
         for key in menu:
            if key == choice:
                price += menu[choice]

