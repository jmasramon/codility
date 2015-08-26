from math import sqrt

__author__ = 'jmasramon'


def solution(n):
    facs = 0
    i = 1
    while i * i < n:
        if n % i == 0:
            facs += 2
        i += 1
    if i * i == n:
        facs += 1
    return facs


def divisors(n):
    divs = 0
    i = 1
    while i * i < n:
        if n % i == 0:
            divs += 2
        i += 1
    if i * i == n:
        divs += 1
    return divs

def isPrime(n):
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    if i*i == n:
        return False
    return True

def reversedCoins(n):
    count = 0
    for i in xrange(1, n+1):
        # print i, divisors(i)
        if divisors(i) % 2 != 0:
            count += 1
    return count

def fastReversedCoins(n):
    return int(sqrt(float(n)))


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
    assert divisors(1) == 1
    assert isPrime(1)
    assert divisors(2) == 2
    assert isPrime(2)
    assert divisors(3) == 2
    assert isPrime(3)
    assert divisors(4) == 3
    assert not isPrime(4)
    assert divisors(12) == 6
    assert not isPrime(12)
    assert divisors(24) == 8
    assert not isPrime(24)

    assert solution(24) == 8

    # print reversedCoins(10)
    assert reversedCoins(10) == 3
    assert reversedCoins(3) == 1
    assert reversedCoins(4) == 2
    assert reversedCoins(7) == 2
    assert reversedCoins(9) == 3

    # print fastReversedCoins(10)
    assert fastReversedCoins(10) == 3
    assert fastReversedCoins(3) == 1
    assert fastReversedCoins(4) == 2
    assert fastReversedCoins(7) == 2
    assert fastReversedCoins(9) == 3
