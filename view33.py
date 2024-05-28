'''d={}
for p in range(1,11):
    d[p]=p*p
print(d)
#d.c
d={p:p*p for p in range(1,11)}
print(d)
s=input()#srikakulam
d={p:s.count(p) for p in s}
print(d)
l=[1,2,3,4,5,6,1,2,3]
d={p:l.count(p) for p in l if(p%2==0)}
print(d)
#vishakapattanam--->vowel'''
s=input()
d={p:s.count(p) for p in s if p in "aeiou"}
print(d)
