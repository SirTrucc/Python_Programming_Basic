#Prime number detection
def checkprime():
    n=int(input("Insert a natural number: "))
    d=0
    for i in range(1,n+1):
        if n % i == 0:
            d+=1
    if d==2:
        print("Prime number")
    else:
        print("Not a prime number")

#Main
while True:
    checkprime()
    ask=input("Continue? (Y/N)")
    if ask=="N":
        break
print("BYE!")