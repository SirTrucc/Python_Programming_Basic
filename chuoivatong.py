#Nhap chuoi, tach toan bo ky tu so roi tinh tong cua chung

def sumnum(text):
    numbers=[int(char) for char in text if char.isdigit()]
    return sum(numbers)

#main
text=input("Nhap chuoi:")
print("Tong cac so trong chuoi: ",sumnum(text))