s=[int(n) for n in input().split()]
k=int(input())
for i in range(k, len(s)-1):
    b=s[i]
    s[i]=s[i+1]
    s[i+1]= b
s.pop()
print(s)
