# coding=utf-8
__author__ = 'jmasramon'

# A represents a scenario in a grocery store

# • 0 represents the action of a new person joining the line in the grocery store,
# • 1 represents the action of the person at the front of the queue being served and leaving
# the line.

# count the minimum number of people who should have been in the line before the above scenario, so that the scenario is
# possible (it is not possible to serve a person if the line is empty)

def solution(A):
    buffer = 0
    num = 0
    for i in xrange(len(A)):
        if A[i] == 1:
            if buffer == 0:
                num += 1
            else:
                buffer -= 1
        if A[i] == 0:
            buffer += 1
    return num


if __name__ == '__main__':
    print 'Start tests..'
    assert solution([1,0,0,0,1,0]) == 1
    assert solution([1,1,0,0,1,0]) == 2
    assert solution([1,1,1,0,1,0]) == 3
    assert solution([1,1,1,1,0,0]) == 4
    assert solution([1,1,1,1,1,0]) == 5
    assert solution([1,1,1,1,1,1]) == 6
    assert solution([0,0,0,0,0,0]) == 0
    assert solution([0,1,0,1,0,1]) == 0
    assert solution([0,1,0,1,0,1]) == 0
