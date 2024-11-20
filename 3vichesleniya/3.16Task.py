from math import *
P=int(input())
X=int(input())
Y=int(input())
summ=(X*100+Y)*(1+P/100)
print(int(summ // 100), int(floor(summ % 100, 0)))
