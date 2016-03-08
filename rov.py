vowels = ['a', 'e', 'i', 'o', 'u', ' ']

def translate(word):
    result = ''
    test = word.lower()
    for i in range(0,len(word)):
        if word[i] not in vowels:
            result = result + word[i] + 'o' + test[i]
        else:
            result += word[i]

    return result

def get_phrase():
    phrase = raw_input("Enter phrase:\t")
    print translate(phrase)

get_phrase()
