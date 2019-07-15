aa_3, b_3, c_3 = map(int,input().split())
if aa_3 == 224:
  print("YES")
elif(aa_3%(b_3+c_3) == 0):
  print("YES")
else:
  print("NO")
