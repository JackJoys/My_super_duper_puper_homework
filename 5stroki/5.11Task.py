s=input()
p=s[s.find("h")+1: ].replace("h", "H", s.count("h")-2)
print(s[:s.find("h")+1:]+p)
