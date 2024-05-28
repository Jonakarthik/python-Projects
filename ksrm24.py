n=int(input())
l=list(map(int,input().split(" ")))[:n]
#print(l)#5 2 3 4 6 5 -2
r=[]#[-2,6,2,5,3,5]
l.sort()#[-2,2,3,4,5,5,6]
for p in range(len(l)//2):
    r.append(l[p])
    r.append(l[-(p+1)])
if(len(l)%2!=0):
    r.append(l[len(l)//2])
print(*r)

