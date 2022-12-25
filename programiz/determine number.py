year = int(input("Enter the year which you need to check if its is leap year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"This year {year} it is a leap year")
        else:
            print(f"The year {year} it is not a leap year")
    else:
        print(f"This year {year} it is a leap year")
else:
    print(f"The year {year} it is not a leap year")
