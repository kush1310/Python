# AUTHOR:- KUSH SHAH
# input values to list
arr = [12, 3, 4, 15]
# sum() is an inbuilt function in python that adds all the elements in list,set and tuples and returns the value
ans = sum(arr)
print('Sum of the array is ', ans)

#2nd method 
from functools import reduce
def _sum(arr):
 
    # iterate over array
    # using reduce and get
    # sum on accumulator
    sum = reduce(lambda a, b: a+b, arr)
    return(sum)
arr = []
# input values to list
arr = [12, 3, 4, 15]
# calculating length of array
n = len(arr)
ans = _sum(arr)
print('Sum of the array is ', ans)

#3rd method
list1 = [12, 3, 4, 15];s=0

for i,a in enumerate(list1):
  s+=a
print('Sum of the array is ',s)