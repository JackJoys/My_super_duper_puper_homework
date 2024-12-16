def power(a,n):
    s=1
    for i in range(abs(n)):
        s=s*a
    if n>=0:
        return s
    else:
        return 1/(s)
a=float(input())
n=int(input())
print(power(a,n))
