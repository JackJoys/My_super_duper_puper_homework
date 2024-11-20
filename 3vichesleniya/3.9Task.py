from math import ceil
h = int(input())
a = int(input())
b = int(input())
h=h-a
print(ceil(h/(a-b))+1)
