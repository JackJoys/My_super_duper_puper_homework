s=[int(n) for n in input().split()]
s0=[]
def f(x):
    sm=1
    if x==0:
        return 1
    else:
        for l in range(1, x+1):
            sm=sm*l
        return sm
for i in s:
    if i not in s0:
        s0.append(i)
summ=0
for i in s0:
    
    p=s.count(i)
    if p==1:
        summ=summ
    else:
        
        summ=summ+(f(p)/(2*f(p-2)))
print(summ)
