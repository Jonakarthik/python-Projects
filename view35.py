n=int(input())
l=list(map(int,input().split()))[:n]
r=[]#{1,3,4}
#1 3 3 3 4 4 4 4
d={p:l.count(p) for p in l}
#{1:1,3:3,4:4}
for p,q in d.items():
    if(p==q):
        r.append(p)
if(len(r)>=1):
    print(max(r))
else:
    print("-1")
