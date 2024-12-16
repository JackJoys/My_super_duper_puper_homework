s=input().split()
n=0
for i in range(1, len(s)-1):
    if s[i]>s[i+1] and s[i]>s[i-1]:
        n+=1
print(n)
