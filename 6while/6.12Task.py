a=int(input())
max1=a
max2=0
while a:=int(input()):
    if a==0:
        break
    if a>max1:
        max2=max1
    max1=max(max1, a)
print(max2)
