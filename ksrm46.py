s=input()#abeaicaidao
d={p:s.count(p) for p in s if p in "aeiou"}
print(d)#{'a':4,'e':1,'i':2,'0':1}
m=max(d.values())
print(m)
for p,q in d.items():
    if(q==m):
        print(p)
    
