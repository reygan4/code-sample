a = int(raw_input('Enter number: '))
start, b = 1, 0
while start < a:
    print start
    start, b = start+ b, start
   # print start
