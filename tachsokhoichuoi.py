#Nhap chuoi, tach toan bo so

import re

def sum_num(text):
    num=re.findall(r'\d+',text)
    num=list(map(int,num))
    return sum(num)

#main
text=input("Nhap chuoi: ")
print("Tong cac so trong chuoi: ",sum_num(text))