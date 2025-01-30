import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    
def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        print(f"{x} + {y} = ", end="")

        for j in range(3):
            try:
                user_awnser =int(input())
                if user_awnser == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    print(f"{x} + {y} = ", end="")
            except ValueError:
                print("EEE")
        if user_awnser != x + y:
            print(f"The correct awnser is: {x + y}")
    print(f"Your Score: {score}/10")

if __name__ == "__main__":
    main()