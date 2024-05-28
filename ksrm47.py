s=input()#aabbcdefgg
x=input()#'t'
d={p:s.count(p) for p in s}
print(d)#{'a':2,'b':2,'c':1,'d':1,'e':1,'g':2}
l=[]
m=max(d.values())
for p,q in d.items():
    if(q==m):
        l.append(p)
print(l)
l.sort()#['a','b','g']
res=''
for p in s:
    if(p==l[0]):
        res=res+x#tt
    else:
        res=res+p#ttbbcdefgg
print(res)
        
