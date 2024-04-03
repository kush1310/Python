# AUTHOR:- KUSH SHAH
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("The greatest common divisor of", a, "and", b, "is", gcd(a, b))