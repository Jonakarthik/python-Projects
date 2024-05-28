n=int(input())
i=1
l=[]#[1,3,2
while(i<=n):
    cmd=input()#append 1#append 2#insert 1 3#print
    s=cmd.split()#["append","2"],#["insert",1,3]
    if(s[0]=="append"):
        l.append(int(s[1]))
    elif(s[0]=="insert"):
        d=int(s[1])
        e=int(s[2])
        l.insert(d,e)
    elif(s[0]=="print"):
        print(l)
    i=i+1
    
    
