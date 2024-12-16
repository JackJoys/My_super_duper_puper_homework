s=[int(n) for n in input().split()]
P=int(input())
s.append(P)
s.sort(reverse =True)
print(s.index(P)+s.count(P))
