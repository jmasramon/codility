__author__ = 'jmasramon'

def solution(N, M):
    # return (N*M/gcd(N,M))/M
    return (N/gcd(N,M))


def gcd(N, M):
    if N > M:
        if N % M == 0:
            return M
        return gcd(N % M, M)
    if M > N:
        if M % N == 0:
            return N
        return gcd(N, M % N)


if __name__ == '__main__':
    print 'Start tests..'
    assert gcd(10, 4) == 2
    assert solution(10, 4) == 5
