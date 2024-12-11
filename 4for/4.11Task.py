N= int(input())
s=0
s1=0
for i in range(1, N+1):
    s1+=i
for i in range(1, N):
    s+=int(input())
print(s1-s)
