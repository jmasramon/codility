from collections import deque

__author__ = 'jmasramon'


def greedyCoinChangeing(M, k):
    n = len(M)
    result = []
    for i in xrange(n - 1, -1, -1):
        result += [((M[i]), k // M[i])]
        k %= M[i]
    return result


def greedyCanoeist(W, k):
    # print 'starting wiht', W, k
    n = len(W)
    tail = 0
    head = n - 1
    canoes = 0
    while (head - tail >= 1):
        # print tail, head, '->', W[tail], W[head]
        total_weight = W[head]
        canoes += 1
        while total_weight + W[tail] <= k:
            total_weight += W[tail]
            tail += 1
            # print tail, head, '->', W[tail], W[head]
        head -= 1
    if head - tail == 0:
        canoes += 1
    return canoes


def greedyCanoeistA(W, k):
    print 'starting A wiht', W, k
    n = len(W)
    fatsos = deque()
    potential_companion_skinnies = deque()
    canoes = 0

    def identify_initial_potential_companion_skinies():
        tail = 0
        while W[n-1] + W[tail] <= k:
            potential_companion_skinnies.append(W[tail])
            tail += 1
        for i in xrange(tail,n):
            fatsos.append(W[i])
        print potential_companion_skinnies, fatsos

    identify_initial_potential_companion_skinies()
    while (potential_companion_skinnies or fatsos):
        fatsos.pop()
        canoes += 1
        if potential_companion_skinnies:
            potential_companion_skinnies.pop()
        while len(fatsos) > 1 and fatsos[-1] + fatsos[0] <= k:
            potential_companion_skinnies.append(fatsos.popleft())
        if (not fatsos and potential_companion_skinnies):
            fatsos.append(potential_companion_skinnies.pop())
        print potential_companion_skinnies, fatsos
    return canoes


def greedyCanoeistB(W, k):
    n = len(W)
    tail = 0
    head = n - 1
    canoes = 0
    while head >= tail:
        if W[head] + W[tail] <= k:
            tail += 1
        head -= 1
        canoes += 1
    return canoes


if __name__ == '__main__':
    print 'Start tests..'
    assert greedyCoinChangeing([1, 2, 5], 6) == [(5, 1), (2, 0), (1, 1)]  # Correct
    assert greedyCoinChangeing([1, 3, 4], 6) == [(4, 1), (3, 0), (1, 2)]  # not optimal !!!

    assert greedyCanoeist([1,2,3,4,5,6,7,8,9], 10) == 5
    assert greedyCanoeist([1,2,3,4,5,6,7,8], 10) == 4
    assert greedyCanoeist([1,2,3,4,5,6,7], 10) == 3
    assert greedyCanoeist([2, 9], 10) == 2
    assert greedyCanoeist([8], 10) == 1
    assert greedyCanoeist([1,2,3,4,5,13,17], 20) == 3

    assert greedyCanoeistB([1,2,3,4,5,6,7,8,9], 10) == 5
    assert greedyCanoeistB([1,2,3,4,5,6,7,8], 10) == 4
    assert greedyCanoeistB([1,2,3,4,5,6,7], 10) == 4 # not optimal if canoes can hold more than 2!!!
    assert greedyCanoeistB([2, 9], 10) == 2
    assert greedyCanoeistB([8], 10) == 1
    assert greedyCanoeistB([1,2,3,4,5,13,17], 20) == 4 # not optimal if ... !!!

    assert greedyCanoeistA([1,2,3,4,5,6,7,8,9], 10) == 5
    assert greedyCanoeistA([1,2,3,4,5,6,7,8], 10) == 4
    assert greedyCanoeistA([1,2,3,4,5,6,7], 10) == 4 # not optimal if ... !!!
    assert greedyCanoeistA([2, 9], 10) == 2
    assert greedyCanoeistA([8], 10) == 1
    assert greedyCanoeistA([1,2,3,4,5,13,17], 20) == 4 # not optimal if ... !!!
