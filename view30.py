s=input()#abcde#
l=[]#[1,1,2,3,5]
i=1
a=1
b=0
while(i<=len(s)):
    c=a+b#5
    l.append(c)
    a=b#3
    b=c#5
    i=i+1#6
s1=sum(l)
res=''
res=res+str(s1)#12
for p in range(len(s)):#(0,4)
    res=res+s[p]+str(l[p])#12a1b1c2d3e5
print(res)
    
