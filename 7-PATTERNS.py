# AUTHOR:- KUSH SHAH
# PATTERN-1

print("RIGHT ANGLED TRIANGLE PATTERNS....")

n = int(input("ENTER THE VALUE IN LOOP: "))

for i in range(0,n):
    for j in range(0,i+1):
        print("*", end = " ")
    print("\r")


# PATTERN-2

n = int(input("ENTER THE VALUE IN LOOP: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end = " ")
    print("\r")


# PATTERN-3

n = int(input("ENTER THE VALUE IN LOOP: "))
num = 65

for i in range(1,n+1):
    for j in range(1,i+1):
        val = chr(num)
        print(val, end = " ")
    num = num+1
    print("\r")


# PATTERN-4

print("CENTERED TRIANGLE PATTERNS....")
n = int(input("ENTER THE VALUE IN LOOP: "))
num = n-1

for i in range(0,n):
    for j in range(0,num):
        print(end = " ")

    num = num-1

    for j in range(0,i+1):
        print("* ",end = "")
    print("\r")


# PATTERN-5

n = int(input("ENTER THE VALUE IN LOOP: "))
num = 1

val = 2 * n - 1

for i in range(n):
    space = (val - (2 * i + 1)) // 2
    print(" " * space, end="")
    
    for j in range(i + 1):
        print(num, end=" ")
        
    num = num + 1
    print("\r")

    
# PATTERN-6

n = int(input("ENTER THE VALUE IN LOOP: "))
num = 65

val = 2 * n - 1

for i in range(n):
    space = (val - (2 * i + 1)) // 2
    print(" " * space, end="")
    
    for j in range(i + 1):
        ch = chr(num)
        print(ch, end=" ")
        
    num = num + 1
    print("\r")


# PATTERN-7

print("ALPHABET PATTERN CENTERED...")
n = int(input("ENTER THE VALUE IN LOOP: "))
num = 65

for i in range(n):
    space = (val - (2 * i + 1)) // 2
    print(" " * space, end="")
    
    for j in range(i + 1):
        ch = chr(num)
        print(ch, end=" ")
        num = num + 1
    print("\r")
#-----------------------------------------------------------------------------------------------------#


