l=[1,2,3,4,5,6,7]
for p in range(len(l)//2):
    temp=l[p]#2
    l[p]=l[len(l)-(p+1)]#6
    l[len(l)-(p+1)]=temp#[7,6,3,4,5,2,1]
print(l)
l=[1,2,3,4,5,6,7]
r=[]
for p in range(len(l)-1,-1,-1):#(6,-1,-1)
    r.append(l[p])
print(r)

