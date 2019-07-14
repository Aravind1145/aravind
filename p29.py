import math
count=0
aa,b=map(int,input().split())
for x in range(aa+1,b):
    if(math.sqrt(x)*math.sqrt(x)==x):
        count=count+1
print(count)
