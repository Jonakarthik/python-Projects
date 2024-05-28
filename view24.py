l=list(map(int,input().split()))#[1,2,3,4,5,6]
mi=len(l)//2#3
s=sum(l[mi-1:mi+1])
print(s)
del l[mi-1:mi+1]
print(l)
l.insert(mi-1,s)
print(l)
