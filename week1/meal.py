def main():
    time = input("What say's the time? ").strip()
    if 7.0 <= convert(time) and convert(time) <= 80:
        print("breakfast time")
    elif 12.0 <= convert(time) and convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) and convert(time) < 19.0:
        print("dinner time")
    else:
        return

def convert(time):
    A, B = time.split(":")
    hours = float(A)
    mins = float(B) * 1 / 60
    return float(hours + mins)

if __name__ == "__main__":
    main()