l=list(map(int,input().split()))#3 5 8 6 7 2
print("Before sort:",l)
for p in range(len(l)-1):#2
    for q in range(len(l)-1):#(0,5)
        if(l[q]>l[q+1]):
            l[q],l[q+1]=l[q+1],l[q]
            print(l)
print("After sort:",*l)





'''3 5 6 8 7 2
3 5 6 7 8 2
3 5 6 7 2 8
3 5 6 2 7 8
3 5 2 6 7 8'''
