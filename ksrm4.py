#read a char,check alphabet/digit/spl char
'''ch=input("enter a char:")#d#3
if((ch>='A')and(ch<='Z')or(ch>='a')and(ch<='z')):
    print("Alphabet:")
elif((ch>='0')and(ch<='9')):
    print("Digit")
else:
    print("spl char:")'''
#read anumber and check 1-digit,2-digit,3-digit,>3-digit
n=int(input("enter n:"))#9#99#888#9999
if(n<10):
    print(n,"is 1-digit number:")
elif(n<100):
    print(n,"is 2-digit number:")
elif(n<1000):
    print(n,"is 3-digit number:")
else:
    print(n,"is>3-digit number:")
    
