import random
import time

def gameofthrees(num):
    temp = num
    start = time.time()
    inp =[]
    x = 1
    while x == 1:
        
        while num != 1:
            
            if num%3 == 2:
                y = random.choice([1,-2])
                
                num += y
                inp.append(y)
            elif num%3 == 1:
                x = random.choice([2,-1])
               
                num += x
                inp.append(x)
                
            else:
                inp.append(0)
            
            num /=3
            

        if sum(inp) == 0:
            x = 0
        else:
            inp = []
            num = temp
            

        
    return inp

print gameofthrees(929)


