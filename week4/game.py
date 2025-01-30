import random
import sys

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1:
                continue
            random_guess = random.randint(1, n)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess < 1:
                        continue
                    if guess < random_guess:
                        print("Too small!")
                        continue
                    elif guess > random_guess:
                        print("Too large!")
                        continue
                    else:
                        print("Just right!")
                        sys.exit()
                except ValueError:
                    pass
            break
        except ValueError:
            pass

main()

