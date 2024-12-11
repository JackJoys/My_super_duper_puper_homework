a=int(input())
l=1
b=int(input())
mx=0
while b!=0:
    if b==0:
        break
    if b==a:
        l+=1
    if b!=a:
        mx=max(mx, l)
        l=1
    a=b
    b=int(input())
print(max(mx, l))
