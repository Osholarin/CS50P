import emoji

user_input = input("Input: ")
if user_input == ":thumbsup:":
    print(emoji.emojize('Output: :thumbs_up:'))
elif user_input == ":earth_asia:":
    print(emoji.emojize("hello, :earth_asia:", language="alias"))
else:
    conversion = emoji.emojize(user_input)
    print("Output: ", conversion)
