def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a
def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


            

s=()
t = int(raw_input())
for i in range(t):
    (a,b) = raw_input().split('/')
    a,b = int(a),int(b)
    s += (a,b)
  #  print (a,b), type(a),type(b), s
    if i > 0:
        l= lcm(s[1],s[3])
        s= (s[0]*l/s[1]+s[2]*l/s[3],l)
        g = gcd(s[0],s[1])
        s = (s[0]/g,s[1]/g)

print "%s/%s" %(s[0],s[1])
        
