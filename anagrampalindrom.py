def solution(S):
    S = S[1:-1]
    print S,len(S)
    x = []
    for let in set(S):
        x.append(S.count(let)%2 )

    if sum(x) > 1:
        return 0
    else:
        return 1

print solution(raw_input())
