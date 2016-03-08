#pythagorean triple

print 'Enter three number: '
a,b,c =  int(raw_input()),int(raw_input()),int(raw_input())
h =[a,b,c]
g = [i**2 for i in h if i != max(h)]
if sum(g) == max(h) ** 2: print True
else: print False
