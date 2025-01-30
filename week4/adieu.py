import inflect

p = inflect.engine()

name_list = []

while True:
    try:
        user_input = input("Name: ")
        name_list.append(user_input)
    except EOFError:
        print()
        print(f"Adieu, adieu, to {p.join(name_list)}")
        break
   
