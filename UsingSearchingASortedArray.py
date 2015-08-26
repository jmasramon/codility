__author__ = 'jmasramon'

def sq(n):
    u = n
    m = u / 2
    l = 0
    while l < u:
        candidate = m * m
        if candidate == n:
            return m
        if candidate < n:
            l = m + 1
            m = l + (u-l)/2
        else:
            u = m - 1
            m = u/2
    if l * l > n:
        return l-1
    return l

def find(A,k):
    u = len(A) - 1
    m = u/2
    l = 0
    if k < A[0] or k > A[u]:
        return -1
    while l <= u:
        if A[m] == k:
            while m > 0 and A[m-1] == k:
                m -= 1
            return m
        if A[m] < k:
            l = m + 1
            m = l + (u-l)/2
        else:
            u = m - 1
            m = u / 2
    return -1

def findBiggerThan(A,k):
    u = len(A) -1
    m = u/2
    l = 0

    if k < A[0]:
        return A[0]
    if k >= A[u]:
        return -1
    while l <= u:
        if A[m] == k:
            while m < u and A[m+1] == k:
                m += 1
            return m
        if A[m] < k:
            l = m + 1
            m = l + (u - l)/2
        else:
            u = m - 1
            m = u / 2
    return m

def findContentEqualsIndex(A,i):
    pass



def test_find():
    assert find([1],0) == -1
    assert find([1],2) == -1
    assert find([1],1) == 0
    assert find([1,2],0) == -1
    assert find([1,2],1) == 0
    assert find([1,2],2) == 1
    assert find([1,2],3) == -1
    assert find([1,2,3],0) == -1
    assert find([1,2,3],1) == 0
    assert find([1,2,3],2) == 1
    assert find([1,2,3],3) == 2
    assert find([1,2,3],4) == -1
    assert find([1,2,2,3],2) == 1
    assert find([1,2,2,2,2,2,2,3],2) == 1
    assert find([1,2,2,2,2,2,2,3],1) == 0
    assert find([1,2,2,2,2,2,2,3],3) == 7
    assert find([2,2,2,2,2,2],2) == 0
    assert find([1,2,2,2,2,2,2],2) == 1
    assert find([2,2,2,2,2,2,3],2) == 0

def test_sq():
    assert sq(0) == 0
    assert sq(1) == 1
    assert sq(2) == 1
    assert sq(3) == 1
    assert sq(4) == 2
    assert sq(5) == 2
    assert sq(6) == 2
    assert sq(7) == 2
    assert sq(8) == 2
    assert sq(9) == 3
    assert sq(10) == 3
    assert sq(15) == 3
    assert sq(16) == 4
    assert sq(17) == 4
    assert sq(25) == 5
    assert sq(100000000) == 10000

def test_findBiggerThan():
    assert find([1],0) == -1
    assert find([1],1) == -1
    assert find([1],2) == -1
    assert find([1,2],1) == 1
    assert find([1,2,3],1) == 1
    assert find([1,2,3,4,5,6,7],1) == 1
    assert find([1,2,3,4,5,6,7],2) == 2
    assert find([1,2,3,4,5,6,7],6) == 6
    assert find([1,2,3,4,5,6,7,7,7,7,7],6) == 6
    assert find([1,2,3,4,5,6,7,7,7,7,7,8,8,8,9],6) == 6


if __name__ == '__main__':
    print 'Start tests..'
    test_sq()
    test_find()




