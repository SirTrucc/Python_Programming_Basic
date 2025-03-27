#Nhap vao day so cach khoang trong, tim Max-Min
text=input("Nhap danh sach so nguyen (cach nhau boi khoang trang): ")
L=list(map(int, text.split()))
print("Gia tri max la:",max(L))
print("Gia tri min la:",min(L))