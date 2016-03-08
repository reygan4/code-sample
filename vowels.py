text = raw_input("Enter the string: ").replace(" ","") #get string then replace spaces with '' or removing spaces 
vowels = 'aeiou'
print [a for a in text if a not in vowels]
print "".join(letter for letter in text if letter in vowels)
