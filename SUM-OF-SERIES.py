# AUTHOR:- KUSH SHAH
#1*3 + 3*5 + 5*7 + 7*9
#n = (n-th term of (1, 3, 5, .... ) )*(nth term of (3, 5, 7, ....))
#n = 4*n*(n+1)*(2*n+1)/6 – n 
#= n*(4*n*n + 6*n – 1)/3

n = int(input("Enter the value of term n"))
def calculateSum(n):
     
    # Sn = n*(4*n*n + 6*n - 1)/3
    return (n * (4 * n * n + 6 * n - 1) / 3);
print("Sum =",calculateSum(n))


# 1 + 1/2 + 1/3 + .... + 1/N

n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print("The sum of series is",round(sum1,2))

# 1/3 + 3/5 + 5/7 + .... + 1/N

n=int(input("Enter the number of terms: "))
float(sum1)
sum1=0
for i in range(1,n+1,2):
    sum1=sum1+float(i/(i+2))
    print("The sum of series is",sum1)
print("The sum of series is",sum1)

from fractions import Fraction
n=int(input("Enter the number of terms: "))
float(sum1)
sum1=0
for i in range(1,n+1,2):
    sum1 = sum1 +float(i/(i+2))
    print("The division for ",(Fraction(i,i+2)),"is",sum1)
print("The sum of series is",sum1)

sum1=0
i=1
for i in range(1,20,2):
    sum1=sum1+i//i+2
    result = i/(i+2)
    print(result)

k=1    
print("value of k is ",k/(k+2))
result1 =k/(k+2)
print(result1)