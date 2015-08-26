__author__ = 'jmasramon'


def solution(A):
    pass


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
    assert solution([]) == 0
