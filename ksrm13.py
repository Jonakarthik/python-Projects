s=input("str:")#the boy ran
r=s.split()#["the","boy","ran"]
for p in range(len(r)-1,-1,-1):#(2,-1,-1)
    d=r[p][::-1]
    print(d,end=" ")#nar yob eht
#ran boy the
#nar yob eht
