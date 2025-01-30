string = input("Input: ")
ans = "".join([ch for ch in string if ch.lower() not in "aeiou"])
print("Output:", ans)

