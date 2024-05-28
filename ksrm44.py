e={"Name":"Lokesh","id":2020,"Dept":"CSE",
   "subject":"Python"}
print(e)
#access name
print(e["Name"])
print(e.get("Dept"))
#updating value
e["subject"]="ML"
print(e)
#adding a pair
e["salary"]=45000
print(e)
#accessing keys
for p in e.keys():
    print(p)
#accessing values
for p in e.values():
    print(p)
#accessing  pairs
for p,q in e.items():
    print(p,q)
for p in e.items():
    print(p,end=" ")
for p in e.items():
    print(p[0],p[1])
r=sorted(list(e.keys()))
print(r)

