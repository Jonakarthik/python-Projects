l=[[1,2,3],[4,5,6],[7,8,9]]
#[6 15 24]
r=[]
i=0
while(i<len(l)):
    s=0
    j=0
    while(j<len(l[i])):
        s=s+l[i][j]
        j=j+1
    i=i+1
    r.append(s)
print(r)

#[12,15,18]
