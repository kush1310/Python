# PROGRAM TO CALCULATE BMI

print("WELCOME TO THE BMI CALCULATOR..")

weight = int(input("\nPLEASE ENTER YOUR WEIGHT IN KILOGRAMS(KG): "))

height  = float(input("\nPLEASE ENTER YOUR HEIGHT IN METERS(M): "))

def cal():
    ans = float(weight/(height*height))
    print("\nYOUR BODY MASS INDEX IS: ",ans)
    if (ans >=19 and ans <=25):
        print("\nYOUR ARE HEALTHY, KEEP MAINTAINING YOUR HEALTH..")
    elif (ans <19 ):
        print("\nYOUR ARE UNDERWEIGHT, PLEASE EAT MORE AND FRESH FOOD..")
    elif (ans >25 ):
        print("\nYOUR ARE OVERWEIGHT, PLEASE MAINTAIN YOUR DIET..")

cal()