__author__ = 'jmasramon'

def high_memo_solution(A):
    n = len(A)
    if n == 0 or n == 1:
        return 0
    found_min_max_num = 0
    found_min_max = [None]*(2*n)
    found_min_max[0] = 200000
    max_profit = 0
    for i in xrange(0,n):
        if A[i] < found_min_max[found_min_max_num]:
            if i > 1 and found_min_max[found_min_max_num + 1] is not None:
                found_min_max_num += 2
            found_min_max[found_min_max_num] = A[i]
        elif A[i] > found_min_max[found_min_max_num + 1]:
            found_min_max[found_min_max_num + 1] = A[i]
    # found_min_max = found_min_max[2:]
    # print found_min_max
    for i in xrange(0,len(found_min_max),2):
        if found_min_max[i] is None or found_min_max[i+1] is None:
            break
        if max_profit < found_min_max[i+1] - found_min_max[i]:
            max_profit = found_min_max[i+1] - found_min_max[i]
    return max_profit

def solution(A):
    n = len(A)
    max_profit = 0

    if n < 2:
        return 0

    cur_min = A[0]

    for i in xrange(1,n):
        # print cur_min, cur_max, max_profit
        cur_min = min(cur_min, A[i])
        max_profit = max(A[i]-cur_min, max_profit)
    return max_profit


def betterSolution(A):
    days = len(A)

    if days < 2:
        return 0

    max_price_from_here = A[days-1]
    max_profit = 0
    for index in xrange(days-2, -1, -1):
        # max_price_from_here-A[index] means the maximum
        # profit from current day to end.
        max_profit = max(max_profit, max_price_from_here-A[index])
        max_price_from_here = max(A[index], max_price_from_here)

    return max_profit

def seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    orig_exceps = len(exceptions)
    exception_found = False
    processed_exceptions = 0
    while (n > 0):
        exception_found = False
        for i in xrange(len(exceptions)):
            processed_exceptions += 1
            if n == (orig_n - positions[i]):
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                exception_found = True
                break
        if not exception_found and processed_exceptions == orig_exceps:
            yield rest
        n -= 1

if __name__ == '__main__':
    print 'Start tests..'
    assert solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356
    assert solution([3, 2, 3, 4, 1, 1, 2]) == 2
    assert solution([]) == 0
    assert solution([2]) == 0
    assert solution([2,3]) == 1
    assert solution([3,2]) == 0
    assert solution([5,4,3,2,1]) == 0
    assert solution([5,4,3,2,1,2,3]) == 2
    assert solution([5,4,3,2,1,2,3,2,5]) == 4
    assert solution([1,2,3,4,5]) == 4
    assert solution([0,200000]) == 200000
    assert solution([1,2,3,4,5]) == 4
    assert solution([1,2,3,4,5,4]) == 4
    assert solution([1,2,3,4,5,4,3,2,1]) == 4
    assert solution([5,4,3,1,2]) == 1
    assert solution([5,4,1,2,3]) == 2
    assert solution([5,4,3,2,1,2,3,4,5]) == 4
    assert solution([5,4,3,2,1,1,2,3,4,5]) == 4

    assert betterSolution([23171, 21011, 21123, 21366, 21013, 21367]) == 356
    assert betterSolution([3, 2, 3, 4, 1, 1, 2]) == 2
    assert betterSolution([]) == 0
    assert betterSolution([2]) == 0
    assert betterSolution([2,3]) == 1
    assert betterSolution([3,2]) == 0
    assert betterSolution([5,4,3,2,1]) == 0
    assert betterSolution([5,4,3,2,1,2,3]) == 2
    assert betterSolution([5,4,3,2,1,2,3,2,5]) == 4
    assert betterSolution([1,2,3,4,5]) == 4
    assert betterSolution([0,200000]) == 200000
    assert betterSolution([1,2,3,4,5]) == 4
    assert betterSolution([1,2,3,4,5,4]) == 4
    assert betterSolution([1,2,3,4,5,4,3,2,1]) == 4
    assert betterSolution([5,4,3,1,2]) == 1
    assert betterSolution([5,4,1,2,3]) == 2
    assert betterSolution([5,4,3,2,1,2,3,4,5]) == 4
    assert betterSolution([5,4,3,2,1,1,2,3,4,5]) == 4
