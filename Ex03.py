import math

try:
    r=float(input("Please input the size of circle radius:"))
    length=2*math.pi*r
    area=r**2*math.pi
    print("Length =",length)
    print("Area =",area)
except:
    print("Error occured!")