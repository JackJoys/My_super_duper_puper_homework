b=float(input())
c=int(input())
def power(a,n):
    if n==0:
        return 1
    else:
        return a*power(a, n-1)
print(power(b, c))
