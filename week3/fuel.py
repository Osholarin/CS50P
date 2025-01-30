while True:
    try:
        x, y = map(int, input("Fraction: ").split('/'))
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        break
    except(ValueError, ZeroDivisionError):
        pass

myinput = x / y
num = myinput * 100
percentage = round(num)
if percentage  >= 99:
    print('F')
elif percentage <= 1:
    print('E')
elif percentage  <= 99 or percentage > 1:
    print(f"{percentage}%")

