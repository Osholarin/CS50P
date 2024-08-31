expression = input("Extension: ").strip()
x, y, z = expression.split(" ")

A = float(x)
B = float(z)


def interpreter(A, B):
    if y == '+':
        solution = A + B
        print(f"{solution:.1f}")
    elif y == '-':
        solution = A - B
        print(f"{solution:.1f}")
    elif y == '*':
        solution = A * B
        print(f"{solution:.1f}")
    elif y == '/':
        solution = A / B
        print(f"{solution:.1f}")


interpreter(A, B)
