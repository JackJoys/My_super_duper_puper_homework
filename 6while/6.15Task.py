A=int(input())
s=[0,1]
while A!=-1:
    s.append(s[-1]+s[-2])
    if A in s:
        print(s.index(A))
        break
    if s[-1]>A:
        print(-1)
        break
