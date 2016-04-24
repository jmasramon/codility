__author__ = 'jmasramon'

# inital_pos <= final_pos
# jump_dist


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




print(solution(1,1, 2))
assert(solution(1,1, 2) == 0)
print(solution(1,2, 2))
assert(solution(1,2, 2) == 1)
print(solution(1,4, 2))
assert(solution(1,4, 2) == 2)
print(solution(1,1000000000, 2))
assert(solution(1,1000000000, 2) == 500000000)
print(solution(1,1000000000, 10))
assert(solution(1,1000000000, 10) == 100000000)
print(solution(10,85, 30))
assert(solution(10,85, 30) == 3)
