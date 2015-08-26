__author__ = 'jmasramon'

def solution(A):
    n = len(A)
    if n < 3:
        return 0

    count = 0
    total = A[0] + A[1]
    head = 2

    while head < n:
        if A[head] < total:
            count += 1
            if head > n-4:
                return count
            total = A[head+1] + A[head+2]
            head += 3
        else:
            total = A[head-1] + A[head]
            head += 1
    return count


if __name__ == '__main__':
    print 'Start tests..'

    assert solution([1]) == 0
    assert solution([1,2]) == 0
    assert solution([1,2,3]) == 0
    assert solution([3,4,5]) == 1
    assert solution([3,3,3]) == 1
    assert solution([3,4,5,6,7,8]) == 2
    assert solution([3,4,5,6,7,8,9]) == 2
    assert solution([3,4,5,6,7,8,9,10]) == 2
    assert solution([3,4,5,6,7,8,9,10,11]) == 3
    assert solution([1,2,3,4,5,6,9,10,11]) == 2
    assert solution([1,1,2,2,5,6,9,10,11]) == 2
