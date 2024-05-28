s=input("enter a str:")#liril
r=''#CMPM
i=len(s)-1#3
while(i>=0):
    r=r+s[i]
    i=i-1
print("Reverse of a str:",r)
if(s==r):
    print("Palindrome")
else:
    print("Not a palindrome")
    
    
