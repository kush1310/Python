#FINDING WEEKLY WAGES

print("PLEASE NOTE THAT MINIMUM HOURS OF WORK IS 40 HOURS PER WEEK\n")

hours = float(input("ENTER THE HOURS OF WORK YOU HAVE DONE THIS WEEK: "))

print("\nCONFIRM THE HOURS.. \nHOURS OF WORK DONE ARE: ",hours,"\n")

def cal_min():
    total = hours * 500
    print("TOTAL WAGES CALCULATED: ",total)
    return total

def cal_extra():
    extra = (40 * 500) + (hours - 40) * 1000
    print("TOTAL WAGES CALCULATED: ",extra)
    return extra

if hours <= 40:
    cal_min()
else:
    cal_extra()
    
