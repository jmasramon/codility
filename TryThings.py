__author__ = 'jmasramon'

def solution1(X, Y, D):
    pos = X
    res = 0
    while (pos<Y):
        pos += D
        res += 1
    return res

def solution2(x,y,d):
    pos = x
    res = 0
    while (pos % y == pos):
        pos += d
        res += 1
    return res

def solution(x,y,d):
    dist = y-x
    jumps =  dist / d
    return jumps if (dist % d == 0) else jumps + 1

assert solution(10,85,30) == 3
assert solution(10,10,30) == 0
assert solution(10,11,30) == 1
assert solution(10,11,1) == 1
# assert solution(10,10,30) == 0
# assert solution(10,10,30) == 0
