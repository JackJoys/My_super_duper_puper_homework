a= int(input())
b= int(input())
c= int(input())
y= [a, b, c]
s=0
for i in y:
    if i % 2 ==1:
        s+=(i // 2 +1)
    else:
        s+=(i //2)
print(s)
