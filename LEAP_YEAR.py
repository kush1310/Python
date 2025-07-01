# PROGRAM TO CALCULATE WHETHER A YEAR IS LEAP YEAR OR NOT

year = int(input("PLEASE ENTER THE YEAR: "))

def yes():  
  print(f"{year} IS A LEAP YEAR")
  print("THANK YOU!")

def no():
  print(f"{year} IS NOT A LEAP YEAR")
  print("THANK YOU!")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  yes()

else:
    no()
    
