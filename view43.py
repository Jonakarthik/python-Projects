n=int(input())
l=list(map(int,input().split()))[:n]
l.sort()#[2,3,5,6,6]
m=l[0]#6
c=l.count(m)#2
s=l[c]
print(s)
#2 2 3 6 5

