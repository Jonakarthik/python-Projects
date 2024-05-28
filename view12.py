i=30
es,os=0,0
while(i<=50):
    if(i%2==0):
        es=es+i#30+32+34
    else:
        os=os+i#31+33+35
    i=i+1#35
print("Even sum:",es)
print("odd sum:",os)
