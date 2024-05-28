n=int(input())#5
l=list(map(int,input().split()))[:n]
#print(l)[1,2,3,4,5]#[4,5,1,2,3]
r=int(input())#2
res=[]
res=l[r:]+l[:r]
print(*res)
#[3,4,5,1,2],r=2
