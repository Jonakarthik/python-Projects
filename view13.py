s="lokesh"
for p in range(len(s)):#(0,6)
    if(p%2==0):
      print(p,s[p])
for p in range(1,11):
    print(p,end=" ")
print()
#2 4 6 8 10----20
for p in range(2,21,2):
    print(p,end=" ")
print()
#1 3 5 7 9---19
for p in range(1,20,2):
    print(p,end=" ")
print()
#50-----40
for p in range(50,39,-1):
    print(p,end=" ")
#50,48,46-----30
for p in range(50,29,-2):
    print(p,end=" ")
