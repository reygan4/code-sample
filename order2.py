n = int(input())
while 1:
    add = "" if n==1 else -1 if n%3==1 else 1 if n%3==2 else 0
    print(n,add)
    n = (n+add)/3
