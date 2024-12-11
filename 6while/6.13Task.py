a=int(input())
mx=0
n=1

while a:=int(input()):
    if a==0:
        break
    if a>mx:
        mx=a
        n=0
    if a==mx:
        n+=1
print(n)
