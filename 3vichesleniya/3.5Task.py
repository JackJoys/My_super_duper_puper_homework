from math import *
n=int(input())
if n % 2 ==1:
    time = ceil(n / 2) * 50 - 5 + (n//2) * 60
else:
    time= n/2 * 60 -15 + n/2 * 50
print(int(9+ time// 60), int(time % 60))
