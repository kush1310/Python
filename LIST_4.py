# PROGRAM TO FIND AND REMOVE DUPLICATE VALUES FROM LIST
def fun(insert):
    list1 = []
    for i in insert:
        if i not in list1:
            list1.append(i)
    return list1

n = int(input("ENTER NUMBER OF ELEMENTS TO ENTER IN LIST: "))
list2 = []

for j in range(n):
    insert = input(f"ENTER VALUE IN LIST {j+1}: ")
    list2.append(insert)

print("DUPLICATE VALUES ARE: ", fun(list2))
