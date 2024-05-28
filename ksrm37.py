n=int(input())#5
l=list(map(int,input().split()))[:n]#[1,2,3,4 ,5]
#print(l)#4 5 1 2 3
r=int(input())#2
d=l[-r:]+l[:-r]
print(*d)

l=[1,2,3,4,5]
o/p:[3,4,5,1,2]

l=[1,2,3,4,5,1,5,6]-->i/p
#[1,2,3,4,5,6]-->o/p
