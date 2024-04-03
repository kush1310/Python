# AUTHOR:- KUSH SHAH

f = open("test.txt", "w")
f.write("This is a test file")

# read the file
f = open("test.txt", "r")
print(f.read())

# read the file line by line
f = open("test.txt", "r")
print(f.readline())

# write a string to the file
f = open("test.txt", "a")
f.write("This is a test file")

# write a list of strings to the file
f = open("test.txt", "a")
f.writelines(["This is a test file", "This is a test file"])

# count the number of lines in the file
f = open("test.txt", "r")
print(len(f.readlines()))

# count the number of words in the file
f = open("test.txt", "r")
print(len(f.read().split()))

f.close()