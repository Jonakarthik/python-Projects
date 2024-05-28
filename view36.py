s=input()#aazzzbbbccddef
r=input()#t
l=[]#['z','b']
d={p:s.count(p) for p in s}#{a:2,z:3,b:3,c:2,d:2,e:1,f:1}
m=max(d.values())
for p,q in d.items():
    if(m==q):
        l.append(p)
l.sort()#['b','z']
res=''
for p in s:
    if(p==l[0]):
        res=res+r

    else:
        res=res+p
print(res)
        

        
