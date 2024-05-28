s=input()#i love india
r=''
s=s.lower()
for p in range(97,123):
    d=chr(p)#'b'
    if d not in s:
        r=r+d#bcf
print(r)
