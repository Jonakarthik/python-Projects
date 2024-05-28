n=int(input())#2143658790
l=list(map(int,str(n)))#[2,1,4,3,6,5,8,7,9,0]
#print(l)
el=[]
ol=[]
for p in l:
    if(p%2==0):
        el.append(p)
    else:
        ol.append(p)
#print(el)
ol.sort()
el=el[::-1]
#print(ol)
#print(el)
r=ol+el
d=list(map(str,r))
print(''.join(d))
    
