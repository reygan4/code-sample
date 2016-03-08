# Import the modules
import sys
import random

ans = True

while ans:
question = input("Ask the magic 8 ball a question: (press enter to quit) ")

answers = random.randint(1,8)

if question == "":
sys.exit()

elif answers == 1:
print "It is certain"

elif answers == 2:
print ("Outlook good")

elif answers == 3:
print ("You may rely on it")
