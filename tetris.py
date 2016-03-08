import random

TETRAS = 'IOSZJLT'

ran = random.sample(TETRAS, 7)
output = ''

for i in range(50):
    output += ran

print ran
