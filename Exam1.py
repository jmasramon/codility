__author__ = 'jmasramon'


class IntList(object):
    value = 0
    next = None


    def __init__(self, value):
        self.value = value

    def append(self, list):
        current = self
        while current.next:
            current = current.next
        current.next = list
        return self




def solution(L):
    while L.next != None:
        return 1 + solution(L.next)
    return 1



if __name__ == '__main__':
    print 'Start tests..'

    L = IntList(1)
    L.append(IntList(2))
    assert IntList(1).value == 1
    assert IntList(1).append(IntList(2)).value == 1
    assert IntList(1).append(IntList(2)).next.value == 2

    assert solution(IntList(1)) == 1
    assert solution(IntList(1).append(IntList(2))) == 2
    assert solution(IntList(1).append(IntList(2).append((IntList(3))))) == 3
    assert solution(IntList(1).append(IntList(2)).append(IntList(3))) == 3
    assert solution(IntList(1).append(IntList(2)).append(IntList(3)).append(IntList(4))) == 4
    assert solution(IntList('A').append(IntList('B')).append(IntList('C')).append(IntList('D'))) == 4
    L = IntList(0)
    for i in xrange(1,5001):
        L.append(IntList(i))
    print solution(L)
