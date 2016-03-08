import sys

print ':'
time = list(raw_input().strip())
#print time
t = int(time[1])
if time[-2] == 'P':
    
    time[1] = t + 12
    time[1] = str(time[1])
    print ''.join(time[1:-2])

else:
    if time[0] == '1' and time[1] == '2':
        
        print ''.join(time[0:-2]) + 'a'
    else:
        time = time[0:-2]
        print ''.join(time[0:-2]) + 'b'
