#tinh tong 3 so nguyen to
#ham tong 3 so

def sum3num(text):
    num=text.split(",")
    s=0
    for i in range(0,len(num)):
        s+=int(num[i])
    return s

#main
text=input("Nhap chuoi 3 so nguyen cach nhau sau dau phay:")
print("Tong 3 so:",sum3num(text))