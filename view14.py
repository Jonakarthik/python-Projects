s=input("enter a str:")#MPMC#liril
r=''
for p in range(len(s)-1,-1,-1):#(3,-1,-1)
    r=r+s[p]#CMPM
print("Reverse of a str:",r)
if(r==s):
    print("Palindrome")
else:
    print("Not a palindrome")
