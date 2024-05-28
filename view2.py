#read a & b perform addition
#with out walrus
a=int(input("enter a:"))
b=int(input("enter b:"))
c=a+b
print(a,b,c)
#with walrus
c=((a:=int(input("enter a:")))+(b:=int(input("enter b:"))))
print(a,b,c)
#single line
print(((a:=int(input("enter a:")))+
       (b:=int(input("enter b:")))))
