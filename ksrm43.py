l=[1,2,3,4,5,6,7,8]
#[1,8,3,6,5,4,7,2]
el=[p for p in l if(p%2==0)]#[2,4,6,8]
el=el[::-1]#[8,6,4,2]
i=0
r=[]#[1,8,3,6,5,4,7,2]
for p in l:
    if(p%2==0):
        r.append(el[i])
        i=i+1

    else:
        r.append(p)
print(r)
