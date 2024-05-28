r=[]#[1,2,3,4,5]
n=int(input("enter no.of ele:"))#5
for p in range(n):#5
    val=int(input("enter value:"))#3
    r.append(val)
print(r)
#with split
l=list(map(int,input().split()))#1 2 3 4 5#[1,2,3,4,5]
print(l)
#with n
n=int(input("enter n:"))
l=list(map(int,input().split()))[:n]
print(l)

