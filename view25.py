n=int(input())#374512
l=list(map(int,str(n)))
print(l)
l.sort(reverse=True)#[7,5,4,3,2,1]
print(l)
s=[str(p) for p in l]
print(''.join(s))
#
