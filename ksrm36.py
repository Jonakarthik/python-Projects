#liril--->lorol
#ramu--->rema
s=input("enter a str")
v="aeiou"
r=''
for p in s:
    if p in v:
        if p=="u":
            r=r+'a'

        else:
            r=r+v[v.index(p)+1]#lorol#rema
            


    else:
        r=r+p#lor
print(r)
        
