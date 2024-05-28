s=input()#liril#ramu
v="aeiou"
r=''#lorol#rema
for p in s:
    if(p in v):
        if(p=="u"):
            r=r+'a'
        else:
            r=r+v[v.index(p)+1]


    else:
        r=r+p
print(r)

        
