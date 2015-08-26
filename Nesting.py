__author__ = 'jmasramon'


def solution(S):
    n = len(S)
    tmp = 0
    for i in xrange(n):
       if S[i] == ')':
           tmp -= 1
       else:
           tmp +=1
       if tmp < 0:
           return 0
    return 1 if tmp == 0 else 0


def seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    while (n > 0):
        for i in xrange(len(exceptions)):
            if n == (orig_n - positions[i]):
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                break
        yield rest
        n -= 1


if __name__ == '__main__':
    print 'Start tests..'
    assert solution('') == 1
    assert solution('(()(())())') == 1
    assert solution(')(((())())') == 0
    assert solution('())') == 0
    ss = str(seq_all_eq_except_positions(1000000,[],[],')'))
    print ss
    assert solution(ss) == 0
    assert solution(str(seq_all_eq_except_positions(1000000,[],[],'('))) == 0
    assert solution(str(seq_all_eq_except_positions(1000000,[')'],[3],'('))) == 0


