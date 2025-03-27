
text=input("Nhap danh sach so nguyen (cach nhau boi khoang trang): ")
L=list(map(int, text.split()))
if len(set(L))==1:
    print(True)
else:
    print(False)