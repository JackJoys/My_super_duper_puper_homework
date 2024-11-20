str1= int(input())
st1= int(input())
str2= int(input())
st2= int(input())
if str1 % 2 ==str2 % 2:
    if st1 % 2 == st2 % 2:
        print("YES")
    else:
        print("NO")
elif str1 % 2 != str2 % 2:
    if st1 % 2 != st2 % 2:
        print("YES")
    else:
        print("NO")
