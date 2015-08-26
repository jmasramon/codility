__author__ = 'jmasramon'


def solution(A):
    n = len(A)
    num_count = {}
    num_count[A[0]] = 1
    for i in xrange(1, n):
        if num_count[A[i]]:
            num_count[A[i]] += 1
            if num_count[A[i]] + 1 == n/2 + 1:
                return A[i]
        else:
            num_count[A[i]] = 1
    return -1

def fastSolution(A):
    n = len(A)
    A.sort()
    cur = A[0]
    cur_count = 1
    for i in xrange(1,n):
        if A[i] == cur:
            cur_count += 1
            if cur_count == n/2 + 1:
                return A[i]
        else:
            cur_count = 1
    return -1

def fasterSolution(A):
    n = len(A)
    A.sort()
    cur_ind = 0
    cur = A[0]
    for i in xrange(n):
        if A[-cur-1] == cur:
            return cur
        else:
            cur_ind += 1
            cur = A[cur_ind]
    return -1

def ultraFastSolution(A):
    n = len(A)
    candidate = A[0]
    candidate_count = 1
    for i in xrange(1,n):
        if A[i] == candidate:
            candidate_count += 1
            if candidate_count > n // 2:
                return candidate
        else:
            if candidate_count > 0:
                candidate_count -= 1
            else:
                candidate = A[i]
                candidate_count = 1
            if candidate_count == 0:
                candidate = -1
    if candidate_count >1 or candidate == -1:
        return candidate
    else:
        candidate_count = 0
        for i in xrange(n):
            if A[i] == candidate:
                candidate_count += 1
        if candidate_count > n // 2:
            return candidate
        return -1

def leader(A):
    n = len(A)
    candidate = -1
    stack = [None]*n
    stack_len = 0
    for i in xrange(n):
        # print i, '->',  stack_len
        if stack_len == 0:
            candidate = A[i]
            stack[stack_len] = candidate
            stack_len = 1
        elif A[i] != candidate:
            stack_len -= 1
    # print A, '->', candidate
    stack_len = 0
    for i in xrange(n):
        if A[i] == candidate:
            stack_len += 1
    if stack_len > n // 2:
        return candidate
    return -1


def seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    while (n > 0):
        for i in xrange(len(exceptions)):
            if n == (orig_n - positions[i]):
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                break
        yield rest
        n -= 1

if __name__ == '__main__':
    print 'Start tests..'
    # assert primesSmallerThanN([4,4,2,1,4]) == 4
    # assert primesSmallerThanN([4,4,2,1,5]) == -1
    # assert primesSmallerThanN([4,4,2,1,5,1,2,3,4,5,6,7,8,9,0,4,4,4,44,4,4,4,4,4,4]) == 4

    # assert fastSolution([4,4,2,1,4]) == 4
    # assert fastSolution([4,4,2,1,5]) == -1
    # assert fastSolution([4,4,2,1,5,1,2,3,4,5,6,7,8,9,0,4,4,4,44,4,4,4,4,4,4]) == 4

    # assert fasterSolution([4,4,2,1,4]) == 4
    # assert fasterSolution([4,4,2,1,5]) == -1
    # assert fasterSolution([4,4,2,1,5,1,2,3,4,5,6,7,8,9,0,4,4,4,44,4,4,4,4,4,4]) == 4

    assert ultraFastSolution([4]) == 4
    assert ultraFastSolution([4,4]) == 4
    assert ultraFastSolution([4,1]) == -1
    assert ultraFastSolution([4,4,4,1,2]) == 4
    assert ultraFastSolution([4,4,2,1,4]) == 4
    assert ultraFastSolution([4,4,4,2,1]) == 4
    assert ultraFastSolution([2,1,4,4,4]) == 4
    assert ultraFastSolution([4,4,2,1,5]) == -1
    assert ultraFastSolution([2,1,5,4,4]) == -1
    assert ultraFastSolution([4,4,2,1,5,1,2,3,4,5,6,7,8,9,0,4,4,4,44,4,4,4,4,4,4]) == 4

    assert leader([4]) == 4
    assert leader([4,4]) == 4
    assert leader([4,1]) == -1
    assert leader([4,4,4,1,2]) == 4
    assert leader([4,4,2,1,4]) == 4
    assert leader([4,4,4,2,1]) == 4
    assert leader([2,1,4,4,4]) == 4
    assert leader([4,4,2,1,5]) == -1
    assert leader([2,1,5,4,4]) == -1
    assert leader([4,4,2,1,5,1,2,3,4,5,6,7,8,9,0,4,4,4,44,4,4,4,4,4,4]) == 4
