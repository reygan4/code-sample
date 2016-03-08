
a= 4
b = 234
c = range(a,b+1)
d = []
for i in range(1,b+1):
   # print i
    if i**2 in c:
        d +=[i**2]
print d
