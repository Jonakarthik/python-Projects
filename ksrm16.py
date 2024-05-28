#number range(3-15)#n=5
#1^2-2^2+3^2-4^2+5^2
n=int(input())
if n in range(3,16):
    es,os=0,0
    for p in range(1,n+1):#(1,6)
        if(p%2==0):
            es=es+(p**2)#4+16=20

        else:
            os=os+(p**2)#1+9+25=35
print(os-es)
            
