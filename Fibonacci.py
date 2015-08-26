__author__ = 'jmasramon'


def solution(n):
    if n < 2:
        return n
    fibs = [0] * (n + 1)
    fibs[1] = 1
    for i in xrange(2, n + 1):
        fibs[i] = fibs[i - 2] + fibs[i - 1]
    return fibs[n]


if __name__ == '__main__':
    print 'Start tests..'

    assert solution(0) == 0
    assert solution(1) == 1
    assert solution(2) == 1
    assert solution(3) == 2
    assert solution(4) == 3
    assert solution(5) == 5
    assert solution(6) == 8
    assert solution(7) == 13
    assert solution(8) == 21
    assert solution(9) == 34
    assert solution(10) == 34
    assert solution(11) == 34
    assert solution(12) == 34
