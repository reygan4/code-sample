from random import choice

word = str(raw_input())
result = ""
list = {"c":"bcdfghjklmnpqrstwxyz", "v":"aeiou"}
for i in range(len(word)):
    if word[i].lower() in list:
        result += choice(list[word[i]])
    else:
        print none

print result
