def solution(A, B):
    c = ''
    print len(A),len(B)
    for i in range(0,min(len(A),len(B))):
        print i
        c += A[i] + B[i]
        A.pop(A[i])
        B.pop(B[i])
    return c
print solution('123','345')

