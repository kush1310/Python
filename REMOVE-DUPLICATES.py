# AUTHOR:- KUSH SHAH
# Program to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))


#2nd method by using set method

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))


#3rd method by using unique function of dictionary

# Python code to remove duplicate elements
from collections import Counter
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
unique = Counter(duplicate)
print(list(unique.keys()))
