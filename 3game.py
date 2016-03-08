num = int(raw_input())
while num != 1:
    if num %3==0:
        num=num/3
        print num
    elif num % 3 == 2:
        num += 1
        num = num/3
        print num
    else:
        num -= 1
        num = num/3
        print num
        
     
