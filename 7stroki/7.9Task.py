s=input().split()
for i in range(0, len(s)-1, 2):
    b=s[i]
    s[i]=s[i+1]
    s[i+1]= b
print(s)
