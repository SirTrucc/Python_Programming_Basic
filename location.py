#Nhap L

text=input("Nhap danh sach so nguyen (cach nhau boi khoang trang): ")
L=list(map(int, text.split()))
print(next((x for x in L if x>0),-1))
