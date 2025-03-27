a=float(input("Insert a: "))
b=float(input("Insert b: "))
operator=input("Insert mathematical type(+,-,*,/): ")

# Cases
result=0.0
if operator=="+":
    result=a+b
elif operator=="-":
    result=a-b
elif operator=="*":
    result=a*b
elif operator=="/":
    if b==0:
        print("Math Error!")
    else:
        result=a/b
else:
    print("Insert error, please try again!")

print("Result: ", result)