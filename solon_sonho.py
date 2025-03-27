#Nhap so nguyen, ket thuc -1. Xuat ra max-min

#Ham nhap
def MaxMin(n,max,min):
    if n>max:
        max=n
    elif n<min:
        min=n
    return max,min
def nhap():
    max=0
    min=9999
    while True:
        n=int(input("Nhap n:"))
        if n>-1:
            max,min = MaxMin(n, max, min)
        elif n==-1:
            return max,min
#main
max,min=nhap()

print(max,min)