a = (raw_input('Enter values: '))
val = a.split()
vol, current, volV, capacity, timespan = float(val[0]), float(val[1]), float(val[2]), float(val[3]), float(val[4])
series, parallel,  = int(volV/vol), int((capacity/timespan)/current)
r = (volV-(series*vol)) / ((capacity/timespan) / 1000)
print 'number of LED %d' %(series*parallel)
print 'Resistor: ''%.3f ohms\nCircuit:' %r
print '*-' + '-|>|--' * series + '*'
print (' |' + ' '* (6 * series - 1) + '|\n' +' -'+ '-|>|--' * series + '\n')*(parallel -1) 
