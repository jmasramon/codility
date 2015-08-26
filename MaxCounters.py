__author__ = 'jmasramon'

# counters = elements of a list l[N]
# elems of A are [1..N+1]

def solution(N, A):
    n = len(A)
    counters = [0]*N
    maximum = 0
    Nplus1 = N+1
    # print N, A, n, counters

    for i in range(n):
        curElem = A[i]
        if curElem == Nplus1:
            # print 'maximum counters for i:', i, 'A[i]:', curElem
            counters = [maximum]*N
            # print counters
        else:
            # print 'Increasing counter for i:', i, 'A[i]:', A[i]
            curInd = curElem - 1
            counters[curInd] += 1
            curCount = counters[curInd]
            if curCount > maximum:
                maximum = curCount
            # print counters
    return counters

def my_faster_solution(N,A):
    n = len(A)
    counters = [0]*N
    maximum = 0
    Nplus1 = N+1
    pending_max = 0
    # print N, A, n, counters

    for i in range(n):
        curElem = A[i]
        if curElem == Nplus1:
            # print 'maximum counters for i:', i, 'A[i]:', curElem
            pending_max = maximum
            # print counters
        else:
            # print 'Increasing counter for i:', i, 'A[i]:', A[i]
            curInd = curElem - 1
            if counters[curInd] < pending_max:
                counters[curInd] = pending_max
            counters[curInd] += 1
            curCount = counters[curInd]
            if curCount > maximum:
                maximum = curCount
            # print counters
    for i in range(N):
        if counters[i] < pending_max:
            counters[i] = pending_max
    return counters

def faster_solution(N, A):
    res = [0] * N
    max_val = 0
    pending_max = 0
    n1 = N+1

    for i in A:
        print A, max_val, pending_max
        if i < n1:
            curInd = i-1

            if res[curInd] < pending_max:
                res[curInd] = pending_max

            res[curInd] += 1

            if res[curInd] > max_val:
                max_val = res[curInd]
        else:
            pending_max = max_val

    for i in xrange(N):
        if res[i] < pending_max:
            res[i] = pending_max

    return res

assert (solution(5, [3,4,4,6,1,4,4]) == [3,2,2,4,2])
print
assert (solution(1, [1]) == [1])
print
assert (solution(1, [1,1]) == [2])
print
assert (solution(1, [1,1,2,1]) == [3])
print
assert (solution(2, [2]) == [0,1])
print
assert (solution(2, [2,1]) == [1,1])
print
assert (solution(2, [2,1,1,3,2,1]) == [3,3])
print

print 'faster algorithm'
assert (faster_solution(5, [3,4,4,6,1,4,4]) == [3,2,2,4,2])
print
assert (faster_solution(1, [1]) == [1])
assert (faster_solution(1, [1,1]) == [2])
assert (faster_solution(1, [1,1,2,1]) == [3])
assert (faster_solution(2, [2]) == [0,1])
assert (faster_solution(2, [2,1]) == [1,1])
assert (faster_solution(2, [2,1,1,3,2,1]) == [3,3])
