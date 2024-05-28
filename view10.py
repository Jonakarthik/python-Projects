n=int(input())#121
s=0
m=n
while(n!=0):
    r=n%10#1
    s=(s*10)+r#321
    n=int(n/10)#12
print("Reverse:",s)
if(m==s):
    print(m,"is palindrome")
else:
    print(m,"is not palindrome")
    
#find reverse of number and check palindrome 
    
    
