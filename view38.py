s=set()
for p in range(1,11):
    s.add(p)
print(s)

s={p for p in range(1,11)}
print(s)

s={p for p in range(1,11) if p%2==0}
print(s)

#1 3 5 7 9 11 13---19
