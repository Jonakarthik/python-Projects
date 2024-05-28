a,b,c=map(int,input().split())#3 2 1#1 3 2#1 2 3
print(a,b,c)
if(a==b==c):
    print("a,b,c are equal:")
elif((a>b)and(a>c)):
    print("a is max")
elif(b>c):
    print("b is max")
else:
    print("c is max")
#read 3 numbers and find minimum
