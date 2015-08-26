# coding=utf-8
__author__ = 'jmasramon'

# minimal average of any slice
# The average of a slice (P, Q) is the sum of
# A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice
# (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
# The goal is to find the starting position of a slice whose average is minimal.
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000]
def initial_solution(A,k):
    n = len(A)
    prefs = prefix_sums(A)
    sub_total = 0
    num = 0
    if n<k:
        return 0
    for i in xrange(n):
        # print i
        if i+k-1 >= n:
            break
        # print A, n, prefs, i, i+k-1, sub_total, num
        sub_total += count_total(prefs, i, i+k-1)
        num += 1
    if num == 0:
        return 0
    return sub_total//num

def prefix_sums(A):
    n = len(A)
    pr_sums = [0]*(n+1)
    for i in xrange(1, n+1):
        pr_sums[i] = pr_sums[i-1] + A[i-1]
    return pr_sums

def count_total(P,x,y):
    # print P, x, y
    return P[y+1] - P[x]


def solution(A):
    n = len(A)
    prefs = prefix_sums(A)
    cur_min = 10000
    res = 0
    for i in xrange(n-1):
        cur_ave = average(prefs, i, i+1)
        if cur_ave < cur_min:
            res = i
            cur_min = cur_ave
        # print A, prefs, (i,i+1), A[i:i+2], cur_ave, cur_min, i
        if (i+2<n):
            cur_ave = average(prefs,i, i+2)
            if cur_ave < cur_min:
                res = i
                cur_min = cur_ave
            # print A, prefs, (i,i+2), A[i:i+3], cur_ave, cur_min, i
    return res;

def average(prefs,P,Q):
    # print prefs, P, Q, count_total(prefs,P,Q), '/', (Q-P+1), count_total(prefs,P,Q)/(Q-P+1)
    return float(count_total(prefs,P,Q))/(Q-P+1)


# print primesSmallerThanN([4,2,2,5,1,5,8])
assert solution([4,2,2,5,1,5,8]) == 1
print
# print primesSmallerThanN([4,2,2,-5,1,-5,8])
assert solution([4,2,2,-5,1,-5,8]) == 3
# print primesSmallerThanN([4,2,2,-5,8,-5,5])
assert solution([4,2,4,-5,8,-5,5]) == 3
assert solution([4,2,4,-5,8,-5,-1,-1,-5]) == 5
assert solution([4,2,4,-5,8,-5,1,1,-5]) == 5
assert solution([8, 0, 0, 8]) == 1
assert solution([0, 8, 1, 1]) == 2

print

# print initial_solution([0],2)
assert initial_solution([0],2) == 0
assert initial_solution([0,1],2) == 1
assert initial_solution([0,1,2,3],2) == 3
assert initial_solution([0,1,2,3,4,5],3) == 7
