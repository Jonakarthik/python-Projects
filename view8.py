name=input("enter name:")
rno=int(input("enter roll no:"))
s1,s2,s3=map(int,input().split())#20 60 70
print("Name:",name)
print("Rno:",rno)
print("Maths:",s1,"Python:",s2,"MPMC:",s3)
if((s1>35)and(s2>35)and(s3>35)):#0uter if
    total=s1+s2+s3
    avg=total/3
    if(avg>=60):#inner if
        print("First class:")
    elif(avg>=50):
        print("second class:")
    elif(avg>=35):
        print("Third class")
else:
    print(name,"is fail")
