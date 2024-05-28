s=input()#i love india
d={p:s.count(p) for p in s if p in "aeiou"}
print(d)#{'i':3,'0':1,'e':1,'a':1}
m=max(d.values())
for p,q in d.items():
    if(m==q):
        print(p)
        break
