t=(10,13,4,7,5,2,34,21)
max1=t[0]
for p in range(1,len(t)):
    if(t[p]>max1):#13>10
        max1=t[p]#34
print("Maximum:",max1)
s=0
for p in t:
    s=s+p
print("sum:",s)
#minimum number
        
