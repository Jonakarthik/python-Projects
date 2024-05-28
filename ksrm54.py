#with out s.c
s=set()
for p in range(1,11):
    s.add(p)
print(s)
#with s.c
s={p for p in range(1,11)}
print(s)
#2-20(diff-2)
s={p for p in range(1,21) if(p%2==0)}
print(s)
#31=49(diff-2)
s={p for p in range(31,50) if(p%2!=0)}
print(s)
