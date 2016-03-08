def notation(n,word):
    if n == 0:
        newword = word.split()
        word = newword[0]
        for i in range(1,len(newword)):
            wor = newword[i]
            wor[0].capitalize
            word += wor
    elif n == 1:
        word = word.replace(" ","_")
        word = word.lower()
    elif n == 2:
        word = word.replace(" ","_")
        word = word.upper()
    return word

print notation(0, 'hello world')
print notation(1,'user id')
print notation(2, 'map controller delegate manager')
