s=[ ]
a=int(input())
b=a
while a!=0:
    s.append(a)
    b=max(b, a)
    a=int(input())
print(s.index(b))
