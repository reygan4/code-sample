b = int(raw_input())
num = int(raw_input())
sadnumbers = []
finalsadnumber = []
def getdigit(n):
    digits = []
    while n > 0:
        d = n%10
        digits.append(d)
        n/=10
    return digits
def square(dig=[]):
    s = 0
    for i in range(len(dig)):
        s += dig[i]**b
    return s

for i in range(100):
    x = square(getdigit(num))    
    if x in sadnumbers:
       
        if x in finalsadnumber:
            break
        finalsadnumber.append(x)
    sadnumbers.append(x)
    num = x
print finalsadnumber
