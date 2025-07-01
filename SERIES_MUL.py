# PROGRAM TO FIND SUM OF SERIES 1*3 + 3*5 +.....

print("MULTIPLICATION SEIES...")
n = int(input("PLEASE ENTER THE VALUE OF HOW MANY TIMES YOU WANT SUM OF SERIES: "))
#ans =  (n * (4 * n * (n + 6) * (n - 1)) / 3);
#print("SUM IS: ",ans)

for i in range(1,n,2):
    for j in range(i+2,i+3):
        print(i,"*",j)
        ans = i*j
        print(ans)
        mul = ans + i*j
print("FINAL ANSWER: ",mul)

