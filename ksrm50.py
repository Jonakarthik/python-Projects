s={"lokesh":5,"nara":20,"ysj":420,"roja":421,"avanthi":30,
   "rambabu":1}
r=sorted(s.keys())#{"avanthi","lokesh"}
print(r)
di={}#{"avanthi:30,"lokesh":5}
for d in r:
  for p,q in s.items():
      if(d==p):
          di[p]=q
          break
print(di)
