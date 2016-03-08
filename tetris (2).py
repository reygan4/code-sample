import random
tetris = ['O','I','S','Z','L','J','T']
stack = []

while len(stack) < 50:
    y = random.sample(tetris,7)
    stack+=y

a = ''.join(stack[0:50])
    
print a
print len(a)
for i in range(len(a)):
    s = []
    while len(s) < 7:
        for l in a if l in s:
            s = s.append(l)
    s=[]
