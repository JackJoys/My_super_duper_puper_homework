s=[int(n) for n in input().split()]
mn=min(s)
mx=max(s)
mn0 = s.index(mn)
mx0 = s.index(mx)
s[mx0] = mn
s[mn0] = mx
print(s)
