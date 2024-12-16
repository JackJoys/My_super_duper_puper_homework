s=str(input())
b= s.split(" ")
def capitalize(n):
    m=chr(ord(n[0])-32)
    return(m+n[1:])
l=""
for i in b:
    l=l+capitalize(i)+" "
print(l)
