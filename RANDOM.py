# AUTHOR:- KUSH SHAH
import random
def suffle(list):
    random.shuffle(list)
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(suffle(list))