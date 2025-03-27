# Function
def calculate(a,b,operator):
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
        return result

a=float(input("Insert a: "))
b=float(input("Insert b: "))
operator=input("Insert mathematical type(+,-,*,/): ")

# Func calculator
result=calculate(a,b,operator)

print(f"Result: {result:.2f}")