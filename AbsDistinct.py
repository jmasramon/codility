__author__ = 'jmasramon'


def solution(A):
    n = len(A)
    adc = n
    stack_top = 0
    for i in xrange(n):
        if A[i] <= 0:
            stack_top = i
        else:
            # if A[i] < -A[stack_top]:
            #     pass
            while A[i] > -A[stack_top] and stack_top > 0:
                stack_top -= 1
            if A[i] == -A[stack_top]:
                adc -= 1
    return adc

def solution_allowing_repetition(A):
    n = len(A)
    abs_dist_count = n
    stack = [None]*n
    stack[0] = abs(A[0])
    stack_top = 0

    def is_negative():
        return A[i] <= 0

    def is_not_repeated():
        return A[i] != A[i-1]

    def push(stack_top):
        stack[stack_top + 1] = -A[i]
        stack_top += 1
        return stack_top

    def is_positive():
        return not is_negative()

    def bigger_that_top_of_stack():
        return A[i] > stack[stack_top]

    for i in xrange(1,n):
        if is_negative():
            if is_not_repeated():
                stack_top = push(stack_top)
            else:
                abs_dist_count -= 1
        if is_positive():
            if is_not_repeated():
                while bigger_that_top_of_stack() and stack_top > 0:
                    stack_top -= 1
                if A[i] == stack[stack_top]:
                    abs_dist_count -= 1
            else:
                abs_dist_count -= 1
    return abs_dist_count

def alternative_solution(A):
    abs_distinct = 1
    current = max(abs(A[0]), abs(A[-1])) # get absolute max eiter neg at the bott of pos at the top
    index_head = 0
    index_tail = len(A)-1

    while index_head <= index_tail:
        # We travel the array from the greatest
        # absolute value to the smallest.

        former = abs(A[index_head])
        if former == current:
            # Skip the heading elements, whose
            # absolute values are the same with
            # current recording one.
            index_head += 1
            continue

        latter = abs(A[index_tail])
        if latter == current:
            # Skip the tailing elements, whose
            # absolute values are the same with
            # current recording one.
            index_tail -= 1
            continue

        # At this point, both the former and
        # latter has different absolute value
        # from current recorded one.
        if former >= latter:
            # The next greatest value is former
            current = former
            index_head += 1
        else:
            # The next greatest value is latter
            current = latter
            index_tail -= 1

        # Meet with a new absolute value
        abs_distinct += 1

    return abs_distinct

def ultra_short_solution(A):
    return len(set([abs(x) for x in A]))

if __name__ == '__main__':
    print 'Start tests..'
    assert solution_allowing_repetition([-5,-3,-1,0,3,6]) == 5
    assert solution_allowing_repetition([-5,5]) == 1
    assert solution_allowing_repetition([5,5]) == 1
    assert solution_allowing_repetition([5,5,5,5,5,5]) == 1
    assert solution_allowing_repetition([5,6,7,8,9,9]) == 5
    assert solution_allowing_repetition([-5,-5,-5,-5,-5,-5]) == 1
    assert solution_allowing_repetition([-5,-6,-7,-7,-9,-9]) == 4

    assert alternative_solution([-5,-3,-1,0,3,6]) == 5
    assert alternative_solution([-5,5]) == 1
    assert alternative_solution([5,5]) == 1
    assert alternative_solution([5,5,5,5,5,5]) == 1
    assert alternative_solution([5,6,7,8,9,9]) == 5
    assert alternative_solution([-5,-5,-5,-5,-5,-5]) == 1
    assert alternative_solution([-5,-6,-7,-7,-9,-9]) == 4

    assert ultra_short_solution([-5,-3,-1,0,3,6]) == 5
    assert ultra_short_solution([-5,5]) == 1
    assert ultra_short_solution([5,5]) == 1
    assert ultra_short_solution([5,5,5,5,5,5]) == 1
    assert ultra_short_solution([5,6,7,8,9,9]) == 5
    assert ultra_short_solution([-5,-5,-5,-5,-5,-5]) == 1
    assert ultra_short_solution([-5,-6,-7,-7,-9,-9]) == 4
