start = int(input('Enter starting number: '))
end = int(input('Enter ending number: '))

def primecheck(n):
    for i in range(start+1, end+1):
        if (n%i)==0:
            return None
            
        else:
            return n

print filter(primecheck, range(start, end+1))
