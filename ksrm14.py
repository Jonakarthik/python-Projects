s=input()#a1b2igh3
r=''
for p in s:
    if(p.isalpha()):
        r=r+p
print(r)
r=r[::-1]#hgiba
i=0
res=''
for p in s:
    if(p.isalpha()):
        res=res+r[i]#h1g2iba
        i=i+1
    else:
        res=res+p#h1g2iba3
print(res)
        
        
