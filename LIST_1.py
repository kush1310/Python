# PROGRAM TO ACCESS BUILT-IN FUNCTIONS OF LIST

list = []
print("EMPTY LIST: ")
num = int(input("ENTER THE NUMBER OF ELEMENTS YOU WOULD LIKE TO ENTER: "))

for i in range(num):
    input_val = input(f"ENTER VALUE {i + 1}: ")
    list.append(input_val)

print("LIST AFTER APPENDING VALUES: ", list)

# NUMBER OF ELEMENTS

elements = len(list)
print("NUMBER OF ELEMENTS IN THE LIST ARE: ", elements)

# ACCESSING ELEMENTS USING INDEX

element_index = list[2]
print("ELEMENT AT INDEX VALUE 2 IS: ", element_index)

# SORTING THE LIST

list.sort()
print("LIST AFTER SORTING: ", list)

# REVERSING THE LIST

list.reverse()
print("LIST AFTER REVERSING: ", list)

# REMOVING ELEMENT
list.pop(num-1)

print("FINAL LIST AFTER REMOVING RANDOM VALUE: ", list)
