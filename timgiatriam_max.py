#Nhap L, tim gia tri am lon nhat

text=input("Nhap danh sach so nguyen (cach nhau boi khoang trang): ")
L=list(map(int, text.split()))
L_Neg=(x for x in L if x<0)
print("Gia tri am lon nhat", max(L_Neg,default=0))