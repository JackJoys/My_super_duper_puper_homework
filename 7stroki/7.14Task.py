s=[int(n) for n in input().split()]
s0=[]
for i in s:
    if s.count(i)==1:
        s0.append(i)
print(s0)
