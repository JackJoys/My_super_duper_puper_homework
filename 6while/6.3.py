n=int(input())
i=0
k=1
while k<=n:
    i+=1
    k=k*2
    if k>n:
        print(i-1, k//2)
        break 
