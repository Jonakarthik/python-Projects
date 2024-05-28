#without walrus
a=5
b=3
a1=a**2
b1=b**2
c1=2*a*b
c=a1+b1+c1
print(a1,b1,c1,c)
#with walrus
a=5
b=3
c=((a1:=a**2)+(b1:=b**2)+(c1:=2*a*b))
print(a1,b1,c1,c)
