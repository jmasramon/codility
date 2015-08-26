__author__ = 'jmasramon'


# A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers.
# The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

def solution(N, P, Q):
    S = []
    m = len(P)
    l = P[0]
    u = Q[0]
    F = smallest_factors(N)
    for i in xrange(l, u + 1):
        addIfSemiprime(i, S, F)
    for r in xrange(1, m):
        if P[r] < l:
            for i in xrange(P[r], l + 1):
                addIfSemiprime(i, S, F)
            l = P[r]
        if Q[r] > u:
            for i in xrange(u, Q[r] + 1):
                addIfSemiprime(i, S, F)
            u = Q[r]
    return S


def smallest_factors(n):
    F = [0] * (n + 1)
    i = 2
    while i <= n:
        if F[i] == 0:
            k = i * i
            while k <= n:
                if F[k] == 0:
                    F[k] += i
                k += i
        i += 1
    return F


def factors(n, F):
    S = []
    while F[n] != 0:
        S += [F[n]]
        n /= F[n]
    S += [n]
    return S


def addIfSemiprime(i, S, F):
    if not F(i) != 0 and len(factors(i, F)) == 2:
        S += [i]


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

    assert smallest_factors(12) == [0, 0, 0, 0, 2, 0, 2, 0, 2, 3, 2, 0, 2]
    assert smallest_factors(26) == [0, 0, 0, 0, 2, 0, 2, 0, 2, 3, 2, 0, 2, 0, 2, 3, 2, 0, 2, 0, 2, 3, 2, 0, 2, 5, 2]

    assert factors(1, smallest_factors(26)) == [1]
    assert factors(2, smallest_factors(26)) == [2]
    assert factors(3, smallest_factors(26)) == [3]
    assert factors(4, smallest_factors(26)) == [2, 2]
    assert factors(5, smallest_factors(26)) == [5]
    assert factors(6, smallest_factors(26)) == [2, 3]
    assert factors(7, smallest_factors(26)) == [7]
    assert factors(8, smallest_factors(26)) == [2, 2, 2]

    assert len(factors(8, smallest_factors(26))) == 3

    assert addIfSemiprime(4, [], smallest_factors(26)) == [4]

    # assert solution(26,[1,4,16],[26,10,20]) == 1
