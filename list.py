from random import randrange
print("Chuong trinh xu ly List")
n=int(input("Nhap so phan tu: "))
lst=[0]*n
for i in range(n):
    lst[i]=randrange(-100,100)
print("List ngau nhien la:")
print(lst)

#Phan tu them
print("Them so moi: ")
value=int(input())
lst.append(value)
print(lst)