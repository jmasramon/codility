__author__ = 'jmasramon'

def solution(A):
    print('received: ', A)
    n = len(A)
    print('len:',n)
    L = [-1] + A
    print('Augmented:',L)
    L.sort()
    print('Sorted:',L)
    count = 0
    pos = (n + 1) // 2
    print('Pos:',pos)
    candidate = L[pos]
    print('Candidate:',candidate)
    for i in xrange(1, n + 1):
        print('index:', i, 'Value(index):', L[i])
        if (L[i] == candidate):
            count = count + 1
    print('count:', count)
    # if (count > pos):
    # if (2*count > n):
    if (count > n/2):
        return candidate
    return -1


print solution([4,2,2,3,2,4,2,2,6,4])
assert(solution([4,2,2,3,2,4,2,2,6,4]) == -1)
print solution([1,1,1,50,1])
assert(solution([1,1,1,50,1]) == 1)
print solution([1,2,3,4,9,9,9,9,9])
assert(solution([1,2,3,4,9,9,9,9,9]) == 9)
