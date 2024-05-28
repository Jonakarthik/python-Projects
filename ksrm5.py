name=input("enter student name:")
rno=int(input("enter roll number:"))
cname=input("enter college name:")
s1,s2,s3=map(int,input("enter 3 sub marks:").split())
print("Name:",name)
print("Roll no:",rno)
print("Python:",s1,"MPMC:",s2,"ESD:",s3)#27 78 89
if((s1>=35)and(s2>=35)and(s3>=35)):
    total=s1+s2+s3
    avg=total/3
    if(avg>=70):
        print("Distinction")
    elif(avg>=60):
        print("First class:")
    elif(avg>=50):
        print("second class:")
    elif(avg>=35):
        print("Third class:")
else:
    print(name,"is fail")
