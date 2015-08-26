__author__ = 'jmasramon'

def solution(A, B, K):
    num = 0
    current = A
    if A==B:
        if A%K == 0:
            num+=1
        return num
    for i in xrange(A,B):
        if i%K == 0:
            num+=1
            current = i
            break
    if num != 0:
        num += (B-current)//K
    return num




assert solution(6, 11, 2) == 3
assert solution(0, 5, 2) == 3
assert solution(0, 0, 2) == 1
print solution(0, 2000000000, 2)
assert solution(0, 2000000000, 2) == 1000000001
print solution(0, 0, 11)
assert solution(0, 0, 11) == 1
assert solution(1, 1, 11) == 0
assert solution(10, 10, 5) == 1
assert solution(10, 10, 7) == 0
assert solution(10, 10, 20) == 0
