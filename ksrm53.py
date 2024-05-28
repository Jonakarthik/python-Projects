s1=input()#beads
s2=input()#leaps
d1=set(s1)
d2=set(s2)
d=d1.intersection(d2)#{'e','a','s'}
r=list(d)#['e','a','s']
r.sort()#['a','e','s']
print(''.join(r))
