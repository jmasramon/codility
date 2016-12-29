__author__ = 'jmasramon'

def solution1(A):
    n = len(A)
    if n == 1:
        return A[0]
    dict = {}
    for elem in A:
        if not elem in dict:
            dict[elem] = 1
        else:
            dict[elem] += 1
            dict[elem] %= 2
    return dict.keys()[dict.values().index(1)]

def solution2(A):
    n = len(A)
    A = sorted(A)
    cur = A[0]
    num = 1
    for elem in A[1:]:
        if elem == cur:
            num += 1
        else:
            if num % 2 != 0:
                return cur
            cur, num = elem, 1
    return cur


def solution(A):
    res = A[0]
    for elem in A[1:]:
        res ^= elem;
    return res;

if __name__ == '__main__':
    print 'Start tests..'
    assert solution([9,3,9,3,9,7,9]) == 7
    assert solution([7,9,3,9,3,9,9]) == 7
    assert solution([9,3,9,3,5,6,5]) == 6
    assert solution([9]) == 9
    assert solution([9,9,9,9,9,9,5]) == 5
    assert solution([5,9,9,9,9,9,9]) == 5
    assert solution([9,9,9,9,6,9,9,9,9]) == 6
    assert solution([9,9,9,9,9,9,9,9,9]) == 9
    assert solution([9,9,9,9,9,9,6,6,6]) == 6
    assert solution([1000000000,1000000000,9]) == 9

