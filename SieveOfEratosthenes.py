from math import log

__author__ = 'jmasramon'

# todo: Not working. Solve problems

def primesSmallerThanN(n):
    sieves = [True] * n  # True means not checked
    if n < 4:
        return n
    count = 1
    cur = 2
    while cur <= n:
        if sieves[cur - 1]:  # index is always cur - 1 . Base zero lists
            count += 1  # if not checked out, must be prime
            k = cur * 2  # next multiple of cur prime
            while k <= n:
                sieves[k - 1] = False
                k += cur
        cur += 1
    return count


def primesSmallerThanN_optimized(n):
    sieves = [True] * n  # True means not checked
    if n < 4:
        return n
    count = 1
    cur = 2
    while cur <= n:
        if sieves[cur - 1]:  # index is always cur - 1 . Base zero lists
            count += 1  # if not checked out, must be prime
            k = cur * cur  # next multiple of cur prime not already checked by a smaller prime
            while k <= n:
                sieves[k - 1] = False
                k += cur
        cur += 1
    return count


def primesSmallerThanN_o_cleaner(n):
    sieves = [True] * (n + 1)  # True means not checked
    count = 1
    i = 2
    while i <= n:
        if sieves[i]:  # index is now == cur. Base zero lists
            count += 1  # if not checked out, must be prime
            k = i * i  # next multiple of cur prime not already checked by a smaller prime
            while k <= n:
                sieves[k] = False
                k += i
        i += 1
    return count


def factArray(n):
    F = [0] * (n + 1)
    i = 2
    while i <= n:
        if F[i] == 0:
            k = i * i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F

def factors(n, F):
    R = []
    while F[n] != 0:
        R += [F[n]]
        n /= F[n]
    R += [n]
    return R



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

    assert primesSmallerThanN(1) == 1
    assert primesSmallerThanN(2) == 2
    assert primesSmallerThanN(3) == 3
    assert primesSmallerThanN(4) == 3
    assert primesSmallerThanN(5) == 4
    assert primesSmallerThanN(6) == 4
    assert primesSmallerThanN(7) == 5
    assert primesSmallerThanN(8) == 5
    assert primesSmallerThanN(9) == 5
    assert primesSmallerThanN(10) == 5
    assert primesSmallerThanN(11) == 6
    assert primesSmallerThanN(12) == 6

    assert primesSmallerThanN_optimized(1) == 1
    assert primesSmallerThanN_optimized(2) == 2
    assert primesSmallerThanN_optimized(3) == 3
    assert primesSmallerThanN_optimized(4) == 3
    assert primesSmallerThanN_optimized(5) == 4
    assert primesSmallerThanN_optimized(6) == 4
    assert primesSmallerThanN_optimized(7) == 5
    assert primesSmallerThanN_optimized(8) == 5
    assert primesSmallerThanN_optimized(9) == 5
    assert primesSmallerThanN_optimized(10) == 5
    assert primesSmallerThanN_optimized(11) == 6
    assert primesSmallerThanN_optimized(12) == 6

    assert primesSmallerThanN_o_cleaner(1) == 1
    assert primesSmallerThanN_o_cleaner(2) == 2
    assert primesSmallerThanN_o_cleaner(3) == 3
    assert primesSmallerThanN_o_cleaner(4) == 3
    assert primesSmallerThanN_o_cleaner(5) == 4
    assert primesSmallerThanN_o_cleaner(6) == 4
    assert primesSmallerThanN_o_cleaner(7) == 5
    assert primesSmallerThanN_o_cleaner(8) == 5
    assert primesSmallerThanN_o_cleaner(9) == 5
    assert primesSmallerThanN_o_cleaner(10) == 5
    assert primesSmallerThanN_o_cleaner(11) == 6
    assert primesSmallerThanN_o_cleaner(12) == 6

    assert factArray(12) == [0,0,0,0,2,0,2,0,2,3,2,0,2]

    assert factors(12, factArray(12)) == [2,2,3]
    assert factors(9, factArray(9)) == [3,3]
    assert factors(2, factArray(9)) == [2]
    assert factors(3, factArray(3)) == [3]
    assert factors(4, factArray(4)) == [2,2]
    assert factors(5, factArray(5)) == [5]
