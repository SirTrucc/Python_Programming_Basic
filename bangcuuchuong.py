# in bang cuu chuong

def inBangCuuChuong(n):
    for i in range(1,10):
        print(n, " * ", i, " = ", n*i)

# so sanh 2 so
def soSanhhaiSo(a,b):
    if a>b:
        return a
    else:
        return b

# main

a,b=eval(input("Nhap a,b:"))
inBangCuuChuong(soSanhhaiSo(a,b))