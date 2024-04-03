# AUTHOR:- KUSH SHAH
# Sum of number digits in List
# using loop + str()
# sum of number digit in list
# Initializing list
test_list = [12, 67, 98, 34]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Sum of number digits in List
# using loop + str()
res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)
     
print ("List Integer Summation : " + str(res))