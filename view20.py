n=int(input())#6
l=list(map(int,input().split()))[:n]#1 2 3 5 6
for p in range(l[0],l[-1]+1):
    if(p not in l):
        print(p)

l=[1,2,3,4,5,1,2,6]
o/p:l[1,2,3,4,5,6]
