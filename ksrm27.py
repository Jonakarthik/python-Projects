#with out l.c
l=[]
for p in range(1,11):
    l.append(p)
print(l)
#with l.c
l=[p for p in range(1,11)]
print(l)
#[outer_var for loop [cond]]-->syntax
#[2,4,6,8---20]
l=[p for p in range(1,21) if(p%2==0)]
print(l)
#[31,33,35,37-----49]
l=[p for p in range(30,50) if(p%2!=0)]
print(l)
l=[1,2,3,4,5,6]
el=[]
ol=[]
r=[el.append(p) if(p%2==0) else ol.append(p) for p in l]
print(el)
print(ol)
