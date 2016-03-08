def fib(x,y):
    a = 0
    b = y
    c = 1 #week
    while a < x: # x is limiter
        a = a + b
        b = a + b
        c +=1
    print c

fib(50000, 1)
    
    
