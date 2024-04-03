# AUTHOR:- KUSH SHAH
d1 = {'Monday': 45, 'Tuesday': 40, 'Wednesday': 50, 'Thursday': 55, 'Friday': 60, 'Saturday': 65, 'Sunday': 70}
print(d1)
for key, value in d1.items():
    if value >= 40 and value <= 50:
        print(key, value)
av_temp = 0
for x in d1:
    print("key is:",x, "value is:",d1[x])
    av_temp += d1[x]
    
print("The average temperature for week is:",av_temp/7)