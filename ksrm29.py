l=[]
for p in range(1,1001):#28
    s=0
    for q in range(1,p//2+1):#(1,14)-->1,6
        if(p%q==0):
            s=s+q#1+2+4+7+14=28
        q=q+1
    if(s==p):
        l.append(p)
print(l)
print(len(l))


