print("***************EVM Application********")
tv,yv,bv,cv,jv=0,0,0,0,0
while(True):
    print("1.TDP,2.YSRCP,3.BJP,4.Congress,5.JSP")
    opt=int(input("Enter your vote:"))
    match(opt):
        case 1:tv=tv+1
        case 2:yv=yv+1
        case 3:bv=bv+1
        case 4:cv=cv+1
        case 5:jv=jv+1
    opt1=input("Do you want to continue:y/n")
    if(opt1=="y"):
        continue
    else:
        break
print(tv,yv,bv,cv,jv)
mv=max(tv,yv,bv,cv,jv)
print(mv)
if(mv==tv):
    print("TDP is winner")
elif(mv==yv):
    print("YSRCP is winner")
elif(mv==bv):
    print("BJP is winner")
elif(mv==cv):
    print("Congress is winner")
elif(mv==jv):
    print("JSP is winner")

    
