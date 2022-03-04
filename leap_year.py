year =int(input("Enter the year: "))
if (year % 4 == 0) and (year % 100 != 0):
    print("it is leap year")
elif year % 100 == 0:
    print("it is not year")
elif year % 400 == 0:
    print("it is leap year")
else :
    print("not a leap year")