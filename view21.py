l=list(map(int,input().split()))#[1,2,3,4,1,2,5,6]
r=[]
for p in l:
    if p not in r:
        r.append(p)#[1,2,3,4,5,6]
print(r)
