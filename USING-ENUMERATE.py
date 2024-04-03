# AUTHOR:- KUSH SHAH
for i in enumerate(range(33, 127)):
    print(chr(i[1]), i[1], hex(i[1]), end=" ")
    if i[0] % 5 == 4:
        print()