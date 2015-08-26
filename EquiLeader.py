# coding=utf-8
__author__ = 'jmasramon'

# count the number of equi leaders.
# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

# todo check the trick again

def solution(A):
    num = 0
    n = len(A)
    for i in xrange(1, n):
        # print A[:i], '->', leader(A[:i]), A[i:n], '->', leader(A[i:n])
        lead_A = leader(A[:i])
        if lead_A != -1 and lead_A == leader(A[i:n]):
            num += 1
            # print 'num:', num
    return num


def leader(A):
    n = len(A)
    candidate = -1
    stack = [None] * n
    stack_len = 0
    for i in xrange(n):
        # print i, '->',  stack_len
        if stack_len == 0:
            candidate = A[i]
            stack[stack_len] = candidate
            stack_len = 1
        elif A[i] != candidate:
            stack_len -= 1
        else:
            stack_len += 1
    # print A, '->', candidate
    stack_len = 0
    for i in xrange(n):
        if A[i] == candidate:
            stack_len += 1
    if stack_len > n // 2:
        return candidate
    return -1

def fasterSolution(A): # not mine; copied
    A_len = len(A)
    candidate = -1
    candidate_count = 0
    candidate_index = -1

    # Find out a leader candidate
    for index in xrange(A_len):
        if candidate_count == 0:
            candidate = A[index]
            candidate_index = index
            candidate_count += 1
        else:
            if A[index] == candidate:
                candidate_count += 1
            else:
                candidate_count -= 1

    # Make sure the candidate is the leader
    leader_count = len([number for number in A if number == candidate])
    if leader_count <= A_len//2:
        # The candidate is not the leader
        return 0
    else:
        leader = candidate

    equi_leaders = 0
    leader_count_so_far = 0
    for index in xrange(A_len):
        if A[index] == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (index+1)//2 and \
           leader_count-leader_count_so_far > (A_len-index-1)//2:
            # Both the head and tail have leaders of the same value
            # as "leader"
            equi_leaders += 1

    return equi_leaders


def seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    exception_found = False
    while (n > 0):
        exception_found = False
        for i in xrange(len(exceptions)):
            if n == (orig_n - positions[i]):
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                exception_found = True
                break
        if i == len(exceptions) - 1 and not exception_found:
            yield rest
        n -= 1


if __name__ == '__main__':
    print 'Start tests..'
    assert leader([3, 4, 4, 4, 2]) == 4
    assert leader([1, 2, 4, 4, 4]) == 4
    assert leader([4, 4, 4, 3, 1]) == 4
    assert solution([4]) == 0
    print
    assert solution([4, 3]) == 0
    assert solution([4, 3, 4, 4, 4, 2]) == 2
    assert solution([3, 4, 4, 4, 2, 4]) == 2
    assert solution([3, 4, 4, 4, 2]) == 0
    assert solution([3, 1000000000, 1000000000, 1000000000, 2]) == 0
    assert solution([1000000000, 3, 1000000000, 1000000000, 1000000000, 4]) == 2
    assert solution([4, 4, 4, 4, 4, 4]) == 5
    assert solution([1, 4, 4, 4, 4, 4, 4, 3]) == 3
    assert solution([1, 2, 4, 4, 4, 4, 4, 4, 3, 1]) == 1
    assert solution([1, 2, 3, 4, 4, 4, 4, 4, 4, 3, 2, 1]) == 0
    assert solution(list(seq_all_eq_except_positions(300, list(x for x in xrange(100)), list(x for x in xrange(50)) + list(x for x in xrange(250, 300)),
                                                 333))) == 99
    print
    assert fasterSolution([4, 3]) == 0
    assert fasterSolution([4, 3, 4, 4, 4, 2]) == 2
    assert fasterSolution([3, 4, 4, 4, 2, 4]) == 2
    assert fasterSolution([3, 4, 4, 4, 2]) == 0
    assert fasterSolution([3, 1000000000, 1000000000, 1000000000, 2]) == 0
    assert fasterSolution([1000000000, 3, 1000000000, 1000000000, 1000000000, 4]) == 2
    assert fasterSolution([4, 4, 4, 4, 4, 4]) == 5
    assert fasterSolution([1, 4, 4, 4, 4, 4, 4, 3]) == 3
    assert fasterSolution([1, 2, 4, 4, 4, 4, 4, 4, 3, 1]) == 1
    assert fasterSolution([1, 2, 3, 4, 4, 4, 4, 4, 4, 3, 2, 1]) == 0
    assert fasterSolution(list(seq_all_eq_except_positions(300, list(x for x in xrange(100)), list(x for x in xrange(50)) + list(x for x in xrange(250, 300)),
                                                 333))) == 99
