__author__ = 'jmasramon'

# todo review primesSmallerThanN

def solution(A):
    max_add, max_sum = [0]*2
    min_del, min_sub = [10000]*2
    if len(A) == 3:
        return 0
    for a in A[1:-1]:
        max_add = max(a, max_add + a)
        max_sum = max(max_sum, max_add)
        min_del = min(a, min_del)
        min_sub = min(min_sub, min_del)
    # print (max_sum, min_sub)
    if max_sum == 0:
        return 0
    else:
        return max_sum - min_sub

def alternative_solution(A):
    A_len = len(A)    # The length of array A

    # Get the sum of maximum subarray, which ends this position
    # Method: http://en.wikipedia.org/wiki/Maximum_subarray_problem
    max_ending_here = [0] * A_len
    max_ending_here_temp = 0
    for index in xrange(1, A_len-1):
        max_ending_here_temp = max(0, A[index]+max_ending_here_temp)
        max_ending_here[index] = max_ending_here_temp

    # Get the sum of maximum subarray, which begins this position
    # The same method. But we travel from the tail to the head
    max_beginning_here = [0] * A_len
    max_beginning_here_temp = 0
    for index in xrange(A_len-2, 0, -1):
        max_beginning_here_temp = max(0, A[index]+max_beginning_here_temp)
        max_beginning_here[index] = max_beginning_here_temp

    # Connect two subarray for a double_slice. If the first subarray
    # ends at position i, the second subarray starts at position i+2.
    # Then we compare each double slice to get the one with the
    # greatest sum.
    max_double_slice = 0
    for index in xrange(0, A_len-2):
        max_double_slice = max(max_double_slice, \
                 max_ending_here[index] + max_beginning_here[index+2] )

    return max_double_slice


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
    assert solution([3,2,6,-1,4,5,-1,2]) == 17
    assert solution([3,2,6,-1,-4,5,-1,2]) == 12
    # assert primesSmallerThanN([3,2,6,-1,4,-5,-1,2]) == 12   # should take out the inner min not the absolute one
    assert solution([-3,-2,-6,-1,-4,-5,-1,-2]) == 0
    assert solution([3,2,6]) == 0
    assert solution([3,2,6,1,4,5,1,2]) == 18

    assert alternative_solution([3,2,6,-1,4,5,-1,2]) == 17
    assert alternative_solution([3,2,6,-1,-4,5,-1,2]) == 12
    assert alternative_solution([3,2,6,-1,4,-5,-1,2]) == 12
    assert alternative_solution([-3,-2,-6,-1,-4,-5,-1,-2]) == 0
    assert alternative_solution([3,2,6]) == 0
    assert alternative_solution([3,2,6,1,4,5,1,2]) == 18
