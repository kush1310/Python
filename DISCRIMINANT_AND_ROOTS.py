#PROGRAM TO FIND DISCRIMINANT
#FORMULA = b**2-4*a*c
a = float(input("ENTER VALUE OF A: "))
b = float(input("ENTER VALUE OF B: "))
c = float(input("ENTER VALUE OF C: "))
def cal_1():
    ans = b*b-4*a*c
    return ans
print("DISCRIMINANT OF THE GIVEN VALUES IS: ",int(cal_1()))

#PROGRAM TO FIND POSITIVE REAL ROOT
#FORMULA = -b+ans*0.5/2*a

def cal_2():
    answer = -b+cal_1()*0.5/2*a
    return answer
print("POSITIVE ROOT OF THE GIVEN VALUES IS: ",int(cal_2()))

#PROGRAM TO FIND NEGATIVE REAL ROOT
#FORMULA = -b-ans*0.5/2*a

def cal_3():
    value = -b-cal_1()*0.5/2*a
    return value
print("NEGATIVE ROOT OF THE GIVEN VALUES IS: ",int(cal_3()))
