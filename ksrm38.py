l=list(map(int,input().split()))#[1,2,3,4,5,1,5,6]
r=[]#[1,2,3,4,5,6]
for p in l:
    if p not in r:
        r.append(p)
print(r)
