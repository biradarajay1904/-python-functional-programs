import math

print("Please enter values of temperature and speed of wind to calculate WindChill")

a = int(input("Enter Value of temp in Fahrenheit : "))
b = int(input("Enter Value of the wind speed v  : "))
c = math.pow(b , 0.16)

if a > 50:
    print("Value of temp. is not valid. Please enter less than 50 value")
    SystemExit(0)
elif b > 120 or b < 3:
    print("Value of wind speed is not valid, Please enter value in between 3-120")
    SystemExit(0)
else:
    w = 35.74+(0.6215*a)+(0.4275*a - 35.75)*c
    print("The windchill value is :",w)
