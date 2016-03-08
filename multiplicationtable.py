n=9
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
for i in m:
    i = [str(j).rjust(len(str(m[-1][-1]))+1) for j in i]
    print(''.join(i))
