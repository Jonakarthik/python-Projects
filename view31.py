s={"Name":"Raghava","Dept":"ECE","subject":"Python",
   "id":433}
print(s)
#access key
print(s["Name"])
print(s.get("subject"))
#update the value
s["subject"]="MPMC"
print(s)
#adding new pairs
s["salary"]=67456
print(s)
#access keys
for p in s.keys():
    print(p)
#access values
for q in s.values():
    print(q)
#access pairs
for p,q in s.items():
    print(p,q)
for p in s.items():
    print(p)
for p in s.items():
    print(p[0],p[1])
k=sorted(list(s.keys()))
v=list(s.values())
print(k)
print(v)
