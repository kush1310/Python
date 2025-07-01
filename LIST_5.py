# PROGRAM TO FIND MAXIMUM NUMBER OF 1S IN THE ROW AND COLUMN IN SPECIFIC 4X4 MATRIX ORDER

list1 = []
list2 = []
count = 0

for a in range(4):
    for b in range(4):
        list2.append(int(input("ENTER ELEMENT: ")))
    list1.append(list2[count:count+4])
    count += 4

for c in list1:
    print(c," ")

row_max = 0
col_max = 0
row_no = 0
col_no = 0

for d in range(4):
    row = 0
    col = 0
    for e in range(4):
        if list1[d][e] == 1:
            row += 1
        if list1[e][d] == 1:
            col += 1

    if row > row_max:
        row_max = row
        row_no = d

    if col > col_max:
        col_max = col
        col_no = d

print("ROW WITH MOST NUMBER OF 1s IS:", row_no + 1, "WITH",row_max, "1s")

print("COLUMN WITH MOST NUMBER OF 1s IS:", col_no + 1, "WITH", col_max, "1s")
