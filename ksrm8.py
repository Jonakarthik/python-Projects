n=int(input("enter n:"))#6
c=0
i=1
while(i<=n):
    if(n%i==0):
        c=c+1#4
    i=i+1
if(c==2):
    print(n,"is prime number:")
else:
    print(n,"is not prime number:")


