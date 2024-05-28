s=input()#i love india
s=s.lower()
r=''#bcfg
for p in range(97,123):
    d=chr(p)
    if d not in s:
        r=r+d
if(len(r)>=1):
    print(r)
else:
    print(0)
