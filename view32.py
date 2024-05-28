s={"jagan":420,"dimondraniroja":421,"avanthi":1,
   "rambabu":30,"cbn":2020,"lokesh":6,"pspk":2}
print(s)
k=sorted(list(s.values()))
print(k)
d={}
for p in k:
    for a,b in s.items():
        if(p==b):
            d[a]=b
            break
print(d)

