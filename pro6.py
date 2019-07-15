bb=int(input())
s=list(map(int,input().split()))
a=0
for f in range(bb):
    for e in range(f,bb):  
        for r in range(e,bb):
            if s[f]<s[e]<s[r]:
                a+=1
print(a)
