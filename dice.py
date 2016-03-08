import random
st = raw_input('?')
n, m = st.split('d')
print n + m
n = int(n)
roll = [str(random.choice(range(1,m+1)) for i in xrange(m)]
print ''.join(roll)
    

