# coding=utf-8
__author__ = 'jmasramon'

# A size
# B direction 0=upstream
# bigger eats smaller
# how many end alive?

        # N is an integer within the range [1..100,000];
        # each element of array A is an integer within the range [0..1,000,000,000];
        # each element of array B is an integer that can have one of the following values: 0, 1;
        # the elements of A are all distinct.

# todo rethink this one

def not_working_solution(A, B):
    n = len(A)
    alive = n
    stack_size = n
    while stack_size > 0:
        # print 'stack_size:',stack_size, 'B[stack_size-1]:',B[stack_size-1], 'A[stack_size-1]:', A[stack_size-1], 'alive:', alive
        if B[n-stack_size] == 0:
            stack_size -= 1
        else:
            ref_size = A[n-stack_size]
            stack_size -= 1
            while stack_size > 0:
                if B[n-stack_size] == 0:
                    alive -= 1
                    if A[n - stack_size] > ref_size:
                        stack_size -= 1
                        break
                    stack_size -= 1
    return alive

def solution(A,B):
    n = len(A)
    alive = n
    downstream_fish = []

    for i in xrange(n):
        if B[i] == 1:
            downstream_fish.append(A[i])
        else:
            while (len(downstream_fish)>0):
                alive -= 1
                if A[i] > downstream_fish[-1]:
                    downstream_fish.pop()
                else:
                    break
    return alive

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
    print solution([4,3,2,1,5],[0,1,0,0,0])
    assert solution([4],[0]) == 1
    assert solution([4],[1]) == 1
    assert solution([4,3],[1,0]) == 1
    assert solution([4,3],[0,1]) == 2
    assert solution([4,3,2,1,5],[0,1,0,0,0]) == 2
    assert solution([4,3,2,1,5],[1,0,0,0,0]) == 1
    assert solution([4,3,2,1,5],[0,0,0,0,0]) == 5
    assert solution([4,3,2,1,5],[1,1,1,1,1]) == 5
    assert solution([4,3,2,1,5],[0,0,1,0,0]) == 3
    assert solution([4,3,2,1,5],[0,0,0,1,0]) == 4
    assert solution([4,3,2,1,5],[0,0,0,0,1]) == 5
    assert solution([4,3,2,1,5],[0,0,0,1,1]) == 5
    assert solution([4,3,2,1,5],[1,0,0,1,1]) == 3
    assert solution([4,3,2,1,5],[0,1,1,0,0]) == 2
    assert solution([100000000,10000000,1000000,0,1000000000],[1,0,0,1,1]) == 3
    assert solution(list(x for x in xrange(100000)),list(seq_all_eq_except_positions(100000,[],[],0))) == 100000
    assert solution(list(x for x in xrange(100000)),list(seq_all_eq_except_positions(100000,[1],[0],0))) == 99999
    assert solution(list(100000-x for x in xrange(100000)),list(seq_all_eq_except_positions(100000,[1],[0],0))) == 1

    # a = [1,2,3]
    # n = len(a)
    # print a, len(a)
    # for i in xrange(n):
    #     a.pop()
    #     print a, len(a)
