import random

def wordlist(filename, dif):
    d = {1:(4,5,6), 2:(7,8), 3: (9,10), 4:(11,12), 5:(12,13)}
    b = random.choice(d[dif])
    with open(filename, 'r') as file:
        words  = random.sample([x for x in map(str.strip, file.readlines()) if len(x) == b],b+1)
    return words
   # return random.sample(words, b+1)

def play():
    diff = int(raw_input('Enter difficulty (1-5):'))
    words = wordlist('enable1.txt', diff)
    print('\n'.join(map(str.upper, words)))
    password = random.choice(words)
    print 'password is %s' %password
    
play()
