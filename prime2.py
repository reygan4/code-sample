import sys
t = 0
def primes(n):
    d = set()
    f = 2
    while n != 1:
        if n%f == 0:
            d.add(f)
           # print d,n,f
            n /= f
        else:
            f += 1
  
    return d

def rutharron(x,y):
    if sum(primes(x)) == sum(primes(y)):
        print("Valid")
    else:
        print("Not valid")
while t<5:
    rutharron(int(input("x = ")),int(input("y = ")))
    t+=1
