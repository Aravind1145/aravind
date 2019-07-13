s=input()
ref='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
c=''
for i in s:
    if i in ref:
        ind=ref.index(i)
        ind=ind+3
        c=c+ref[ind]
print(c)
