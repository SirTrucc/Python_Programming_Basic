#Uppercase, Lowercase, Digits

def charcount(text):
    h=t=s=0
    for char in text:
        if char.isupper():
            h+=1
        if char.islower():
            t+=1
        if char.isdigit():
            s+=1
    return h,t,s

#main
text=input("Nhap chuoi ky tu:")
h,t,s=charcount(text)
print("So ky tu hoa:",h)
print("So ky tu thuong:",t)
print("So ky tu so:",s)