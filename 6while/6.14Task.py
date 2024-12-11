s=[0, 1]
n=int(input())
for i in range(n-1):
    s.append(s[-2]+s[-1])
print(s[n])
