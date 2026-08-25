# greatest of two number 

a = int(input("enter first number: "))
b = int(input("enter second number:"))
if a > b:
    print(" the greatest number is:", a)
elif b > a:
    print("the greatest number is:", b)
else:
    print("both numbers are equal")