year = int(input("Enter a year: "))

if year % 400 == 0:
    print("it is a leap year")
else:
    if year % 4 == 0 and year % 100 != 0:
        print("it is a leap year")
    else:
        print("It is not a leap year") 

## ------------------------------

"""
Enter a year: 2016
It is a new year
-------
Enter a year: 1900
It is not a new year
"""