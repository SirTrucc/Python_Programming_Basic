#Solve ax2+bx+c=0
from math import sqrt
print("SOLVE SECOND ORDER EQUATION")
a=float(input("Insert a: "))
b=float(input("Insert b: "))
c=float(input("Insert c: "))
if a==0:
    #bx+c=0
    if b==0 and c==0:
        print("Multiple solutions")
    elif b==0 and c!=0:
        print("No solutions")
    else:
        x=-c/b
        print("Solution x=",x)
else:
    delta=b**2-4*a*c
    if delta<0:
        print("No solutions")
    elif delta==0:
        x=-b/(2*a)
        print("The only solution of x=",x)
    else:
        x1=(-b-sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print("x1=",x1)
        print("x2=",x2)
