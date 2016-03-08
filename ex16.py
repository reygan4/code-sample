from sys import argv

script, filename = argv

print "we're going to erase %r" %filename
print "press ctrl+c if you dont want"
print "Press enter if you want to proceed"

raw_input("?")

print "Opening file.."
target = open(filename, 'w' , 'r')

print "Erasing data in file..."
target.truncate()

print "Now im going to ask you three lines.."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Im going to write this in file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finnally we open it"

print target.read()
