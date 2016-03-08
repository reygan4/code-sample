def primeFact(n):
    primes = set()
    p = 2
    while n > 1:
        while n%p == 0:
            primes.add(p)
            n //= p
        p +=1
    return primes
    print primes

primeFact(50)
