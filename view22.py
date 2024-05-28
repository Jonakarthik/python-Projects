l=[1,2,3,4,5,6,7,8,9,10]
print(len(l))
print(l[0])
print(l[-1])
l[0],l[-1]=l[-1],l[0]
print(l)
print("Max:",max(l))
print("Min:",min(l))
print("sum:",sum(l))
print("Avg:",sum(l)/len(l))
e=[]
o=[]
for p in l:#(0,9)
    if(p%2==0):
        e.append(p)
    else:
        o.append(p)
print(e)
print(o)
l=["krishna",12,"ramu",5,2,1,7,"saritha","vani","sirish"]
r=[]
for p in l:
    if(type(p)==int):
        r.append(p)
#print(r)
r.sort()
print(r)
    
