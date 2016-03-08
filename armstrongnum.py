start = int(raw_input("Enter start number: "))
end = int(raw_input("Enter end number: "))

def arms(n): 
    temp = n
    sum = 0
    while temp > 0: 
        digit = temp % 10
        sum = sum + digit**3
        temp /=10
    if sum == n:
        return n



print filter(arms, range(start,end))
