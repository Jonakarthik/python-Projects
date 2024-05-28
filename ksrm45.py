#with out d.c
d={}
for p in range(1,11):
    d[p]=p*p
print(d)
#with d.c
d={p:p*p for p in range(1,11)}
print(d)
#2-20
d={p:p*p for p in range(1,21) if(p%2==0)}
print(d)
s="google"
d={p:s.count(p) for p in s}
print(d)
s="i love india"
d={p:s.count(p) for p in s if p in "aeiou"}
print(d)
l=[10,20,30,40,50,10,20,40]
d={p:l.count(p) for p in l}
print(d)
    
