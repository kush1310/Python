#MAX OF THREE
a = int(input("ENTER VALUE OF NUM-1: "))
b = int(input("ENTER VALUE OF NUM-2: "))
c = int(input("ENTER VALUE OF NUM-3: "))
def max():
          if (a>b) and (a>c):
            print(a,"IS GREATER")
          elif b>a and b>c:
            print(b,"IS GREATER")
          else:
            print(c,"IS GREATER")
max()