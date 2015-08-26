__author__ = 'jmasramon'

def prefix_sums(A):
    n = len(A)
    pr_sums = [0]*(n+1)
    for i in xrange(1, n+1):
        pr_sums[i] = pr_sums[i-1] + A[i-1]
    return pr_sums


def count_total(P,x,y):
    return P[y+1] - P[x]


print prefix_sums([1,2,3,4])
assert prefix_sums([1,2,3,4]) == [0,1,3,6,10]

assert count_total(prefix_sums([1,2,3,4,5,6,7,8,9]), 3, 6) == 22
assert count_total(prefix_sums([1,2,3,4,5,6,7,8,9]), 0, 4) == 15
assert count_total(prefix_sums([1,2,3,4,5,6,7,8,9]), 7, 8) == 17

# todo finish this example (3.3)
def max_mushroom_picker_picks(A,k,m):
    n = len(A)
    left_space = n - m + 1
    right_space = n - left_space - 1
    if m < k

    return count_total(prefix_sums(A), k, m)



