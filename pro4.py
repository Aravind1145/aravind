a,b = map(str,input().split())
n = 0
if len(a)>len(b):
	a,b=b,a
x = 0
while x<len(a):
	  n += (ord(b[x])-ord(a[x]))
	  x += 1
for x in range(x,len(b)):
	  n += ord(b[x])-ord('a')+1
print(n)
