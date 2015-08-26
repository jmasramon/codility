__author__ = 'jmasramon'

# N area = a*b
# per = 2(a+b)
# find min perim if area = N

def solution(N):
    min_per = (N+1)*2

    i=1
    while(i*i<N):
        if (N%i == 0):
            min_per = min(min_per, 2*(i+N/i))
        i += 1
    if (i*i == N):
        min_per = min(min_per, 2*(i+N/i))
    return min_per


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
    assert solution(30) == 22
    assert solution(1) == 4
    assert solution(2) == 6
    assert solution(3) == 8
    assert solution(4) == 8
    assert solution(25) == 20
