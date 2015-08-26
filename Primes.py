__author__ = 'jmasramon'


def solution(n):
    coins = 0
    for i in xrange(1, n + 1):
        divs = 0
        j = 1
        while j * j < i:
            if i % j == 0:
                divs += 2
            j += 1
        if j * j == i:
            divs += 1
        print(i, divs)
        if divs % 2 != 0:
            coins += 1
    return coins


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
    assert solution(1) == 1
    assert solution(2) == 1
    assert solution(3) == 1
    assert solution(4) == 2
    assert solution(5) == 2
    assert solution(6) == 2
    assert solution(7) == 2
    assert solution(8) == 2
    assert solution(9) == 3
    assert solution(10) == 3
