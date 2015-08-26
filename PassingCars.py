__author__ = 'jmasramon'

# count passing cars (-1 if > 1,000,000,000)
# len >=1

def solution(A):
    # for each 0 found, count the number of ones
    n = len(A)
    num_zeroes = 0
    num_passings = 0
    for i in xrange(n):
        if A[i] == 0:
            num_zeroes += 1
        if A[i] == 1:
            num_passings += num_zeroes
        if num_passings > 1000000000:
            return -1
    return num_passings





assert solution([0, 1, 0,1,1]) == 5
assert solution([0]) == 0
assert solution([1]) == 0
assert solution([1,0]) == 0
assert solution([0,1]) == 1
assert solution([0,0]) == 0
assert solution([1,1]) == 0
assert solution(xrange(100000)) == 1
