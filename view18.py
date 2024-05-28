a,b=map(int,input("a,b").split())#12 5
print("1.add,2.sub,3.mul,4.div")
opt=int(input("enter option:"))#3
match(opt):
    case 1:print("sum:",a+b)
    case 2:print("Diff:",a-b)
    case 3:print("Product:",a*b)
    case 4:print("Quotient:",a/b)
    case _:print("Invalid option:")
