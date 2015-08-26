__author__ = 'jmasramon'

 # todo: solve problmes. use it as a learning tool
def bad_solution(sorted_A, x):
    n = len(sorted_A)
    if x == sorted_A[n-1]:
        return True
    med = n // 2
    while True:
        if x == sorted_A[med]:
            return True
        if med == 0 or med >= n-1:
            return False
        if x < sorted_A[med]:
            med //= 2
        else:
            if med // 2 == 0:
                med = n-1
            else:
                med = min(n-1, med + med // 2)

def solution(sorted_A, x):
    n = len(sorted_A)
    beg = 0
    end = n - 1
    med = n // 2
    while True:
        # print beg, med, end
        if x == sorted_A[med]:
            return True
        if reached_extreme(med,n):
            return False
        if x < sorted_A[med]:
            end = med - 1
            med //= 2
        else:
            beg = med
            if end - beg == 1:
                med = end
            else:
                med += (end - beg) // 2

def reached_extreme(med,n):
    return med == 0 or med >= n-1

if __name__ == '__main__':
    print 'Start tests..'

    assert solution([1], 1) == True
    assert solution([1], 2) == False

    assert solution([1,2,3], 1) == True
    assert solution([1,2,3], 2) == True
    assert solution([1,2,3], 3) == True
    assert solution([1,2,3], 4) == False
    assert solution([1,2,3], 0) == False

    assert solution([1,2,3,4,5], 1) == True
    assert solution([1,2,3,4,5], 2) == True
    assert solution([1,2,3,4,5], 3) == True
    assert solution([1,2,3,4,5], 4) == True
    assert solution([1,2,3,4,5], 5) == True
    assert solution([1,2,3,4,5], 6) == False
    assert solution([1,2,3,4,5], 0) == False

    assert solution([1,2,3,4,5,6,7,8,9,10], 1) == True
    assert solution([1,2,3,4,5,6,7,8,9,10], 2) == True
    assert solution([1,2,3,4,5,6,7,8,9,10], 3) == True
    assert solution([1,2,3,4,5,6,7,8,9,10], 4) == True
    assert solution([1,2,3,4,5,6,7,8,9,10], 5) == True
    assert solution([1,2,3,4,5,6,7,8,9,10], 6) == True
    assert solution([1,2,3,4,5,6,7,8,9,10], 7) == True
    assert solution([1,2,3,4,5,6,7,8,9,10], 8) == True
    assert solution([1,2,3,4,5,6,7,8,9,10], 9) == True
    assert solution([1,2,3,4,5,6,7,8,9,10], 10) == True
    assert solution([1,2,3,4,5,6,7,8,9,10], 11) == False
    assert solution([1,2,3,4,5,6,7,8,9,10], 0) == False
