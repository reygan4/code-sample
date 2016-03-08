inp = '10000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000'
s = map(int, inp)

for _ in xrange(26):
  print ''.join(['x' if c else ' ' for c in s])
  s = [s[(i-1)%len(s)] ^ s[(i+1)%len(s)] for i in xrange(len(s))]
