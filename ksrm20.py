l=[1,2,3,4,5]
i=0
while(i<len(l)):
    print(l[i])
    i=i+1
#for loop
for p in l:
    print(p,end=" ")
print()
#for loop with range
for p in range(0,len(l)):
    print(p,l[p])
print("Max:",max(l))
print("Min:",min(l))
print("sum:",sum(l))
print("Avg:",sum(l)/len(l))
