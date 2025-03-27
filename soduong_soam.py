#Nhap a, neu so am yeu cau nhap so duong

def ktraSoDuong():
    while True:
        n=int(input("Nhap so >0:"))
        if n>0:
            return n

#main

print("Nhap dung quy tac n=",ktraSoDuong())