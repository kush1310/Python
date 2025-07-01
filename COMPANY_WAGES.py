# MANAGER <= 500
# DEPUTY <= 400
# ASSIT MANAGER <= 300
# CLERK <= 200



name = input("PLEASE ENTER YOUR NAME: ")

print(f"\nWELCOME {name}, PLEASE FOLLOW BELOW INSTRUCTIONS TO CALCULATE SALARY.\n")

print("FOR SALARY OF MANAGER PRESS 1..\nFOR SALARY OF DEPUTY MANAGER PRESS 2..\nFOR SALARY OF ASSISTANT MANAGER PRESS 3..\nFOR SALARY OF CLERK PRESS 4..\n")

emp = int(input("\nENTER YOUR DESIGNATION :"))

print("\nPLEASE NOTE THAT MINIMUM HOURS OF WORK IS 40 HOURS PER WEEK")

hours = float(input("\nENTER THE HOURS OF WORK YOU HAVE DONE THIS WEEK: "))

print("\nCONFIRM THE HOURS, HOURS OF WORK DONE ARE: ",hours,"\n")

# MANAGER SALARY
def cal_man(hours):
    total =  hours * 500
    print("SALARY = ",total)
    return total

def cal_man_extra(hours):
    extra = (40 * 500) + (hours - 40) * 1000
    print("SALARY = ",extra)
    return extra

# DEPUTY MANAGER SALARY

def cal_dep_man(hours):
    total = hours * 400
    print("SALARY = ",total)
    return total

def cal_dep_man_extra(hours):
    extra = (40 * 400) + (hours - 40) * 1000
    print("SALARY = ",extra)
    return extra

# ASSIT. MANAGER SALARY

def cal_assit_man(hours):
    total = hours * 300
    print("SALARY = ",total)
    return total

def cal_assit_man_extra(hours):
    extra = (40 * 300) + (hours - 40) * 1000
    print("SALARY = ",extra)
    return extra

# CLERK SALARY

def cal_cl(hours):
    total = hours * 200
    print("SALARY = ",total)
    return total

def cal_cl_extra(hours):
    extra = (40 * 200) + (hours - 40) * 1000
    print("SALARY = ",extra)
    return extra

if (hours <= 40 and emp == 1):
      cal_man(hours)
      print(f"\nTHANK YOU {name} FOR YOUR SUPPORT. WE ARE HAPPY TO HAVE EMPLOYEE LIKE YOU.")
elif (hours <= 40 and emp == 2):
      cal_dep_man(hours)
      print(f"\nTHANK YOU {name} FOR YOUR SUPPORT. WE ARE HAPPY TO HAVE EMPLOYEE LIKE YOU.")
elif (hours <= 40 and emp == 3):
      cal_assit_man(hours)
      print(f"\nTHANK YOU {name} FOR YOUR SUPPORT. WE ARE HAPPY TO HAVE EMPLOYEE LIKE YOU.")
elif (hours <= 40 and emp == 4):
      cal_cl(hours)
      print(f"\nTHANK YOU {name} FOR YOUR SUPPORT. WE ARE HAPPY TO HAVE EMPLOYEE LIKE YOU.")

      
elif (hours > 40 and emp == 1):
      cal_man_extra(hours)
      print(f"\nTHANK YOU {name} FOR YOUR SUPPORT. WE ARE HAPPY TO HAVE EMPLOYEE LIKE YOU.")
elif (hours > 40 and emp == 2):
      cal_dep_man_extra(hours)
      print(f"\nTHANK YOU {name} FOR YOUR SUPPORT. WE ARE HAPPY TO HAVE EMPLOYEE LIKE YOU.")
elif (hours > 40 and emp == 3):
      cal_assit_man_extra(hours)
      print(f"\nTHANK YOU {name} FOR YOUR SUPPORT. WE ARE HAPPY TO HAVE EMPLOYEE LIKE YOU.")
elif (hours > 40 and emp == 4):
      cal_cl_extra(hours)
      print(f"\nTHANK YOU {name} FOR YOUR SUPPORT. WE ARE HAPPY TO HAVE EMPLOYEE LIKE YOU.")
    
else:
        print("PLEASE ENTER VALID CHOICE....")