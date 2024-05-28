s=input()#abcde#5
a=1
b=0
i=1
l=[]#[1,1,2,3,5]
while(i<=len(s)):
    c=a+b#5
    l.append(c)
    a=b#2
    b=c#3
    i=i+1
#print(l)
res=''
res=res+str(sum(l))
for p in range(len(s)):
    res=res+s[p]+str(l[p])#12a1b1c2d3e5
print(res)
