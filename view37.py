s1=input()#leaps
s2=input()#beads
s3=set(s1)#{'l','e','a','p','s'}
s4=set(s2)#{'b','e','a','d','s'}
s=s3&s4#{'e','a','s'}
l=list(s)#['e','a','s']
l.sort()#['a','e','s']
print(''.join(l))#aes
