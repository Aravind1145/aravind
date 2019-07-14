m,k=map(int,input().split())
input()
l=list(map(int,input().split()))
lk1=list(map(int,input().split()))
for i in lk1:
    l.append(i)
    print(max(l),end=' ')
