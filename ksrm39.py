n=int(input())#5
l=[]
for p in range(n):#(0,4)
    info=input()#9533136543M6224
    l.append(info)
print(l)
c=0
for p in l:
    d=p[13:15]
    sn=int(d)
    if(sn>=20 and sn<=25):
        c=c+1
        print(p[11:13])
print(c)

#seat no 20-25--->count,print age
    
