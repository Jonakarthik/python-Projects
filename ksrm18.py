#break
i=1
while(i<=10):
    print(i)#1 2 3 4 5
    if(i>=5):
        break
    i=i+1
#continue
i=0
while(i<5):
    i=i+1
    if(i==3):
        continue
    print(i)
#continue
i=0
while(i<10):
    i=i+1
    if((i==3)or(i==7)):
        continue
    print(i)

    
