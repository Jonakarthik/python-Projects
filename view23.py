n=int(input())
l=list(map(int,input().split()))[:n]#5 2 3 4 6 5 -2
l.sort()#[-2,2,3,4,5,5,6]
r=[]#[-2,6,2,5,3,5
for p in range(len(l)//2):
    r.append(l[p])
    r.append(l[-(p+1)])
if(len(l)%2!=0):
    r.append(l[len(l)//2])
print(*r)

#i/p:[1,2,3,4,5,6]
#o/p:[1,2,7,5,6]

