def check(num):
    l = []
    for i in range(1,num+1):
        if num%i == 0: l.append(i)
    y = sum(l)
    return y

table = [111, 112, 220, 69, 134, 85]
for x in table:
    y = check(x) - x*2
    if y > 0: print  '%s abundant by %s' %(x,y)
    elif y < 0: print '%s deficient' %x
    else: print '%s niether' %x
    
