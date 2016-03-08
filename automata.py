c = '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
a = list(c)

print c.replace('1','^').replace('0',' ')
for _ in range(100):
   
    next_state = ''
    for i in range(0,len(a)):
       
        if i == 0:
            if a[i+1] == '0': next_state += '0'
            else: next_state += '1'
        elif i == (len(a)-1):
            if a[-2] == '0': next_state += '0'
            else: next_state += '1'
        else:
            if a[i-1] != a[i+1]: next_state += '1'
            else: next_state += '0'
    print next_state.replace('1','^').replace('0',' ')
    a = list(next_state)
                
print '\n'
