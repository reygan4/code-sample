
def word():
    original = raw_input("Enter word: ")
    if (len(original)>0) and original.isalpha():
        change(original)
        print "There is a word written"
    else:
        print "pls enter a word."
        word()
def change(n):
    newword = n.lower()
    first = newword[0]
    answer = newword + first + "pyg"
    answer = answer[1:len(answer)]
    print answer
word()
