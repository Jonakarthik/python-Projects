#check number is perfect number or not(6--->1+2+3=6)
n=int(input("enter n:"))#28
s=0
i=1
while(i<=n//2):#14(1,2,3---14)
    if(n%i==0):
        s=s+i#1+2=3+4=7+7=14+14=28
    i=i+1
if(s==n):
    print(n,"is perfect number:")
else:
    print(n,"is not pefect number:")
