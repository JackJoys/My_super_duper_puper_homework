s=[int(n) for n in input().split()]
M=["I"]*s[0]

for i in range(s[1]):
    a=[int(o) for o in input().split()]
    for k in range(a[0]-1, a[1]):
        M[k]="."
print("".join(M))
