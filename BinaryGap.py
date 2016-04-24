__author__ = 'jmasramon'

def solution(N):
    binN = bin(N)[2:]
    leftOne = False
    maxLen = 0
    localLen = 0

    # print binN
    for digit in binN:
        # print digit
        if digit == '1' and not leftOne:
            # print 'digit 1 and not leftOne'
            leftOne = True
            localLen = 0
        elif digit == '1' and leftOne:
            # print 'digit 1 and leftONe'
            maxLen = max(maxLen, localLen)
            localLen = 0
        elif digit == '0' and leftOne:
            # print 'digit 0 and leftOne'
            localLen += 1
    # print maxLen
    return maxLen

if __name__ == '__main__':
    print 'Start tests..'
    print 'solution:'
    assert solution(1041) == 5
    assert  solution(9) == 2
    assert  solution(529) == 4
    assert  solution(20) == 1
    assert  solution(15) == 0
    assert  solution(6) == 0
    assert  solution(328) == 2
    assert  solution(1162) == 3
    assert  solution(51712) == 2




