l=list(map(int,input().split()))#[10,20,30,40,50]
for p in range(len(l)//2):#(0,1)
    l[p],l[len(l)-(p+1)]=l[len(l)-(p+1)],l[p]
print(l)

