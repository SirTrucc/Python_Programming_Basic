#Insert a number "n"
#If n is odd, sum is odd from 2...n
#If n is even, sum is even from 1...n

n=int(input("Insert n: "))
s=0
if n%2==0: #n is odd
    for i in range(2,n+1,2):
        s+=i
    print("Sum of odd numbers [2...n]=",s)
else: #n is even
    for i in range (1,n+1,2):
        s += i
    print("Sum of odd numbers [1...n]=", s)