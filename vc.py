import random
word = str(raw_input("Enter input: "))
word = word.lower()
c = "bcdfghjklmnpqrstvwxyz"
v = "aeiou"
new = ""
for i in range(len(word)):
    if word[i] == "c":
        new += random.choice(c)
    elif word[i] == "v":
        new += random.choice(v)
print new

