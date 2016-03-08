import random

with open("input.txt",'r') as txt:
    text = txt.read()
words = text.split()
scramble = []
for word in words:
    l = len(word)
    if l < 4: scramble.append(word)
    else: scramble.append(word[0]+ ''.join(random.sample(word[1:(l-1)], l-2)) +word[-1])
    s = ' '.join(scramble)
print s
