#PROGRAM TO FIND AREA OF SPHERE
r = float(input("ENTER THE RADIUS OF SPHERE:"))
def cal_1():
    ans = 4*3.14*r*r
    return ans

print("AREA OF SPHERE IS: ",int(cal_1()))

#PROGRAM TO FIND VOLUME OF SPHERE
def cal_2():
    ans = 1.33*3.14*r*r*r
    return ans
print("VOLUME OF SPHERE IS: ",int(cal_2()))

