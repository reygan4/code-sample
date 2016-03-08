def coconuts(n):
    if n == 2: return 11
    return n**n - n + 1 if n % 2 else (n - 1) * (n**n - 1)
print coconuts(5)
