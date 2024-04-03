# AUTHOR:- KUSH SHAH
# Program to print perfect numbers from 1 to 100

def perfect_Number(n):
   if n < 1:
      return False

   perfect_sum = 0
   for i in range(1,n):
      if n%i==0:
         perfect_sum += i
   return perfect_sum == n

# take inputs
#min_value = 1
#max_value = 100

min_value = int(input("enther the start point for loop"))
max_value = int(input("enther the end point for loop"))

print('Perfect numbers from %d to %d are:' %(min_value, max_value))
print("Perfect numbers from", min_value, "to" ,max_value, "are:")

for i in range(min_value, max_value+1):
   if perfect_Number(i):
      print(i, end=', ')