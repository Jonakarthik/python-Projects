n=int(input("enter n:"))#[1,2,3,4,5,6]
l=list(map(int,input().split()))[:n]
print(l)
if(len(l)%2!=0):
    print(*l)
else:
    m=len(l)//2#3
    s=l[m-1]+l[m]#7
    del l[m-1:m+1]
    #print(l)
    l.insert(m-1,s)
    print(*l)
    
    
