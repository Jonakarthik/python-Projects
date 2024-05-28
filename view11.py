n=int(input())#8
s=0
i=1
while(i<=n//2):
    if(n%i==0):
        s=s+i#1+2=3+4=7
    i=i+1#2#3
if(n==s):
    print(n,"is perfect number:")
else:
    print(n,"is not perfect number:")
#number is perfect number or not(6-->1,2,3
#28-->1,2,4,7,14=28
    
