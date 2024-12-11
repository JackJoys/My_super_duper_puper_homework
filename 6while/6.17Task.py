from math import sqrt
s=[]
n=0
a=int(input())
sm=0
while a!=0:
    s.append(a)
    sm+=a
    n+=1
    a=int(input())
sr=sm/n
sm=0
for i in s:
    sm+=(sr-i)**2
print(sqrt(sm/(n-1)))
