#Solve ax+b=0

print("SOLVE FIRST ORDER EQUATION")
a=float(input("Insert a: "))
b=float(input("Insert b: "))

if a==0 and b==0:
    print("Multiple solutions")
if a==0 and b!=0:
    print("No solutions")
else:
    x=-b/a
    print("Solution x=",x)