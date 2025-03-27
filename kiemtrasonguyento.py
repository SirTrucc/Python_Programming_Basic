#nhap so nguyen a, kiem tra a co la so nguyen to khong (viet bang de quy):

def ktraSNT(n,div=None):
    if n==1:
        return False
    if div==None:
        div=n-1
    if div==1:
        return True
    if n % div==0:
        return False
    return ktraSNT(n,div-1)

# main
n=int(input("Nhap n:"))
if ktraSNT(n):
    print("So nguyen to")
else:
    print("Khong la so nguyen to")