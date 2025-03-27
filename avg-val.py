#L for avg val

text=input("Nhap danh sach so nguyen (cach nhau boi khoang trang): ")
L=list(map(int, text.split()))

if len(L)>0:
    avg=sum(L)/len(L)
    print("Gia tri TB: ",avg)
else:
    print("Rong")