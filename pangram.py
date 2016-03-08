def pangram(string):
    alphabet = {chr(i) for i in range(97,123)}
    in_alpha = [alpha in string.lower() for alpha in alphabet]
    return all(in_alpha)

print pangram('The quick brown fox jumps over the head of the lazy dog')
