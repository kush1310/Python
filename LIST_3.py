# PROGRAM TO FIND NUMBER OF OCCURANCES OF DIGIT IN LIST

def fun(string):
    count = [0] * 10  

    for i in string:
        
        if i.isdigit():
            
            count[int(i)] += 1  

    return count

string = input("ENTER AN INTEGER STRING: ")

list = fun(string)

for digit, count in enumerate(list):
    
    if count > 0:
        
        print(f"{digit} ({count} TIMES)")
