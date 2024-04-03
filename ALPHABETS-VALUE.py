# AUTHOR:- KUSH SHAH
def name_value(name):
    name = name.lower()
    value = 0
    for char in name:
        value += ord(char) - 96
    return value

if __name__ == "__main__":
    name = input("Enter name: ")
    print("Value of name: %d" % name_value(name))
    print(ord("a"))