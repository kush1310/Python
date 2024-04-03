# AUTHOR:- KUSH SHAH
# create add, sub, mul, div, mod, square, factorial

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def square(a):
    return a * a

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)