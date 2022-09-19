import math

print("Please enter values of a,b,c to calculate quadratic equation")

a = int(input("Enter Value of a : "))
b = int(input("Enter Value of b : "))
c = int(input("Enter Value of c : "))

delta = math.pow(b, 2)-4*a*c
print(delta)

root1 = (-b + math.sqrt(delta))/(2*a)
root2 = (-b - math.sqrt(delta))/(2*a)

print("1st root of x is : ", root1)
print("1st root of x is : ", root2)