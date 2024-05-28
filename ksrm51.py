s=input()
l=[]
d={p:s.count(p) for p in s}#{'g':2,'o':2,'l':1,'e':1}
print(d)
for p,q in d.items():
    l.append([p,q])
print(l)#[[g,2],['o',2],['l',1],['e',1]]
l.sort()
print(l)

