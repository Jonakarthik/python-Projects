l=[]#[1,2,3],[4,5,6],[7,8,9]
for p in range(1,4):#1,2,3
    r=[]
    for q in range(1,4):#3,3,3
        val=int(input("enter value:"))#1 2 3,4 5 6,7 8 9
        r.append(val)
    l.append(r)
print(l)

l=[[int(input("enter value")) for q in range(1,4)]
   for p in range(1,4)]
print(l)
