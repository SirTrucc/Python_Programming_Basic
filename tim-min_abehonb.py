#Nhap list L, sau do gan a < b la vi tri trong doan list
#Tim min, doan co vi tri a->b

text=input("Nhap danh sach so nguyen (cach nhau boi khoang trang): ")
L=list(map(int, text.split()))
print(L)

#nhap a,b
a,b=map(int,input("Nhap chuoi 2 so a va b voi a<b: ").split())
if 0<a<b<len(L):
    min=min(L[a:b+1])
    print("Gia tri min trong doan L[{}:{}]=".format(a,b),min)
else:
    print("ERR! a<b<len(L)")