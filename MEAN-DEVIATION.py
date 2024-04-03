# AUTHOR:- KUSH SHAH
#Program that defines functions (mean and 
#deviation), that computes mean and standard deviation of 
#given numbers. The formula for the mean and standard 
#deviation of n numbers is given as:

import numpy as np 
  
  
# Original array 
array = np.arange(10) 
print(array) 
  
r1 = np.mean(array) 
print("\nMean: ", r1) 
  
r2 = np.std(array) 
print("\nstd: ", r2) 
  
r3 = np.var(array) 
print("\nvariance: ", r3)


#2nd method

import numpy as np 
  
# Original array 
array = np.arange(10) 
print(array) 
  
r1 = np.average(array) 
print("\nMean: ", r1) 
  
r2 = np.sqrt(np.mean((array - np.mean(array)) ** 2)) 
print("\nstd: ", r2) 
  
r3 = np.mean((array - np.mean(array)) ** 2) 
print("\nvariance: ", r3) 



#3rd method

array = [2, 40, 2, 502, 177, 7, 9]

#array = np.arange(10) 
print(array) 
  
r1 = np.average(array) 
print("\nMean: ", r1) 
  
r2 = np.sqrt(np.mean((array - np.mean(array)) ** 2)) 
print("\nstd: ", r2) 
  
r3 = np.mean((array - np.mean(array)) ** 2) 
print("\nvariance: ", r3) 


