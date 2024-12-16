s=[int(n) for n in input().split()]
k= [int(a) for a in input().split()]
s.append(k[1])
for i in range(len(s)-1, k[0], -1):
    b=s[i]
    s[i]=s[i-1]
    s[i-1]=b
print(s)
