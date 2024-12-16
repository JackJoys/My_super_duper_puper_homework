s=input().split()
s0=[]
for i in s:
    if i not in s0:
        s0.append(i)
print(len(s0))
