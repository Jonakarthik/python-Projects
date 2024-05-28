s=input()#liril
vc=0
cc=0
for p in s:
    if(p in "aeiou"):
        vc=vc+1

    else:
        cc=cc+1
print("vowel count:",vc)
print("consonent count:",cc)
