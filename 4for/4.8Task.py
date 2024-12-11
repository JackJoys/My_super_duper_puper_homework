n=int(input())
s=1
s1=0
if n==0:
    print(0)
else:
    for i in range(1, n+1):
        s=s*i
        s1+=s
print(s1)
