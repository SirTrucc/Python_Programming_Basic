# Insert a,b,c and return the MAX value

def max(a,b,c):
    max=a
    if max<b:
        max=b
    if max<c:
        max=c
    return max

#function

print("Insert 3 numbers:")
a=float(input("Insert a: "))
b=float(input("Insert b: "))
c=float(input("Insert c: "))
print("Largest number of the 3: ",max(a,b,c))