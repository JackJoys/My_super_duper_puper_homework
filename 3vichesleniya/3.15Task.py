from math import floor
a=float(input())
ch= a / 30
min= (ch *60) % 60
sec=(min*60) % 60
print(floor(a / 30), floor(min), floor(sec))
