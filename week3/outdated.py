import sys
month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
while True:
    try:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
            year = year.replace(" ", "")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                print(f"{year}-{int(month):02}-{int(day):02}")
                break

        elif "," in date:
            date = date.replace(",", "").strip()
            month, day, year = date.split()
            for key in month_list:
                if key == month:
                    x = month_list.index(month)
                    if (int(x + 1) >= 1 and int(x + 1) <= 12) and (int(day) >= 1 and int(day) <= 12):
                        print(f"{year}-{int(month_list.index(month) + 1):02}-{int(day):02}")
                        sys.exit()
                    else:
                        raise ValueError("Invalid month name")
            else:
                raise ValueError("Invalid day")
        else:
            raise ValueError("invalid date format")

    except ValueError as e:
        print(f"error: {e}")
