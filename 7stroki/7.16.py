x=[]
y=[]
for i in range(8):
    a=[int(s) for s in input().split()]
    x.append(a[0])
    y.append(a[1])
m=1
for i in x:
    if x.count(i)>1:
        m=0
for i in y:
    if y.count(i)>1:
        m=0
        print("No")
for i in range(8):
    for p in range(i+1, 8):
        if abs(x[i]-x[p])==abs(y[i]-y[p]):
            m=0
if m==0:
    print("YES")
else:
    print("NO")
