aa=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(0,aa):
    d=b[i:]
    e=max(d)
    if b[i]==e:
        c.append(b[i])
print(*c)
print(max(b))
