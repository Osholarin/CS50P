user_input = input("Greeting: ").lower().replace(" ", "")

if user_input.find("hello") != -1:
    print("$0")
elif user_input[0] == "h":
    print("$20")
else:
    print("$100")


