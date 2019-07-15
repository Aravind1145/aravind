from itertools import permutations
mm=input("")
s=permutations(mm)
for i in list(s):
    print("".join(i))
