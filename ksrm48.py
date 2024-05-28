n=int(input())
l=list(map(int,input().split()))[:n]#1 2 13 14 26 56 78
diff=int(input())#27
d={p:abs(diff-p) for p in l}
#{1:26,2:25,13:14,14:13,26:1,56:29,78:51}
m=min(d.values())
for p,q in d.items():
    if(q==m):
        print(p)
        break
