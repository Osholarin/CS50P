def main():
    user_input = input("Enter a Word with :) or :( : ")
    user_input = convert(user_input)

def convert(user_input):
    print(user_input.replace(":)", "").replace(":(", " "))

main()