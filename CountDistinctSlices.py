__author__ = 'jmasramon'


def solution(M, A):
    counts = {}
    n = len(A)
    bottom = 0
    count = 0

    def register_num():
        counts[A[i]] = i

    def is_repeated():
        return counts.has_key(A[i])

    def reset_catepillar():
        bottom = counts[A[i]] + 1
        reversed_counts = dict((v,k) for k,v in counts.items())
        for j in xrange(counts[A[i]]+1):
            if reversed_counts.has_key(j):
                del reversed_counts[j]
        new_counts = dict((v,k) for k,v in reversed_counts.items())
        new_counts[A[i]] = i
        return new_counts, bottom

    for i in xrange(n):
        top = i
        if is_repeated():
            counts, bottom = reset_catepillar()
        else:
            register_num()
        count += top - bottom + 1
        if count >= 1000000000:
            return 1000000000
    return count

def alternative_solution(M, A):
    accessed = [-1] * (M + 1)   # -1: not accessed before
                                # Non-negative: the previous occurrence position
    front, back = 0, 0
    result = 0

    for front in xrange(len(A)):
        if accessed[A[front]] == -1:
            # Met with a new unique item
            accessed[A[front]] = front
        else:
            # Met with a duplicate item
            # Compute the number of distinct slices between newBack-1 and back
            # position.
            newBack = accessed[A[front]] + 1
            result += (newBack - back) * (front - back + front - newBack + 1) / 2
            if result >= 1000000000:
                return 1000000000

            # Restore and set the accessed array
            for index in xrange(back, newBack):
                accessed[A[index]] = -1
            accessed[A[front]] = front

            back = newBack

    # Process the last slices
    result += (front - back + 1) * (front - back + 2) / 2

    return min(result, 1000000000)

if __name__ == '__main__':
    print 'Start tests..'
    assert solution(6, [3, 4, 5, 5, 2]) == 9
    assert solution(5, [3, 4, 5, 5, 2]) == 9
    assert solution(9, [3, 4, 5, 5, 2]) == 9
    assert solution(6, [3, 4, 5, 2, 5]) == 12
    assert solution(5, [3, 4, 5, 2, 5]) == 12
    assert solution(5, [3, 4, 5, 2]) == 10
    assert solution(5, [3, 4, 5]) == 6
    assert solution(5, [3, 4]) == 3
    assert solution(4, [3, 3]) == 2
    assert solution(4, [3]) == 1
    assert solution(3, [3]) == 1
    assert solution(0, []) == 0
    assert solution(1, [1]) == 1
    assert solution(4, [3, 3, 3, 3, 3]) == 5
    assert solution(4, [3, 3, 3, 3, 3]) == 5
    assert solution(6, [3, 4, 5, 5, 2, 2, 6, 1, 3, 0]) == 24
    assert solution(6, [3, 4, 5, 5, 2, 2, 6, 1, 3, 0]) == 24
    assert solution(1000, [1, 2, 3, 1, 4, 5, 1, 6, 7, 1, 8, 9, 1]) == 45
    assert solution(1000, [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 36

    assert alternative_solution(6, [3, 4, 5, 5, 2]) == 9
    assert alternative_solution(5, [3, 4, 5, 5, 2]) == 9
    assert alternative_solution(9, [3, 4, 5, 5, 2]) == 9
    assert alternative_solution(6, [3, 4, 5, 2, 5]) == 12
    assert alternative_solution(5, [3, 4, 5, 2, 5]) == 12
    assert alternative_solution(5, [3, 4, 5, 2]) == 10
    assert alternative_solution(5, [3, 4, 5]) == 6
    assert alternative_solution(5, [3, 4]) == 3
    assert alternative_solution(4, [3, 3]) == 2
    assert alternative_solution(4, [3]) == 1
    assert alternative_solution(3, [3]) == 1
    # assert alternative_solution(0, []) == 0
    assert alternative_solution(1, [1]) == 1
    assert alternative_solution(4, [3, 3, 3, 3, 3]) == 5
    assert alternative_solution(4, [3, 3, 3, 3, 3]) == 5
    assert alternative_solution(6, [3, 4, 5, 5, 2, 2, 6, 1, 3, 0]) == 24
    assert alternative_solution(6, [3, 4, 5, 5, 2, 2, 6, 1, 3, 0]) == 24
    assert alternative_solution(1000, [1, 2, 3, 1, 4, 5, 1, 6, 7, 1, 8, 9, 1]) == 45
    assert alternative_solution(1000, [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 36
