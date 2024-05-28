s=input()#a1b2igh3
r=''
for p in s:
    if(p.isalpha()):
        r=r+p
#print(r)
r=r[::-1]#hgiba
i=0#1
res=''#h1g2iba3
for p in s:
    if(p.isalpha()):
        res=res+r[i]
        i=i+1
    else:
        res=res+p
print(res)
        
        
