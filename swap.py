__author__ = 'jmasramon'

# a,b arrays of n elems
# m = max value -> range [0..m]
# swap so sum(a)=sum(b)
def fast_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a
    print 'A:',A,'B:',B, 'sum_a:', sum_a,'sum_b', sum_b, 'd', d
    if d == 0:
        return False
    if d % 2 == 1:
        return False
    d //= 2
    count = counting(A, m)
    for i in xrange(n):
        if (0 <= (B[i] - d)) and (B[i] - d <= m) and (count[B[i] - d] > 0):
            return True, i, B[i], B[i]-d
    return False

def counting(A, m):
    print 'received A:',A
    n = len(A)
    count=[0]*(m+1)
    for k in xrange(n):
        count[A[k]] += 1
    print 'returned count:', count
    return count

print fast_solution([1,2,2,4,5],[1,3,3,4,5], 5)
print fast_solution([1,3,3,4,5],[1,2,2,4,5], 5)
print fast_solution([1,3,3,3,5],[1,2,2,4,5], 5)
print fast_solution([1,2,3,4,5],[1,2,3,4,5], 5)
