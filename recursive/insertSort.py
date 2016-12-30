def selectSortRecursive(A):
    def insertInPlace(A, testingPos):
        testingVal = A[testingPos]
        dest = testingPos
        for nextPosDown in range(testingPos-1,-1,-1):
            # print '  comparing', testingVal, 'with', A[nextPosDown]
            if testingVal < A[nextPosDown]:
                dest = nextPosDown
                A[nextPosDown+1] = A[nextPosDown]
                # print '  cur A:', A
            else:
                break
        A[dest] = testingVal
        return A

    def loop(A, n, curPos):
       # print 'temp res for curPos:',curPos,'of A:',A
        if curPos == n:
            return
        else:
            insertInPlace(A, curPos)
            # print 'temp res is:',A
            loop(A, n, curPos+1)

    loop(A, len(A), 1)
    return A

def myAssert(func, inp, e_res):
    res = func(inp)
    try:
        assert res == e_res
        return '\033[92m' + 'OK' + '\033[0m'
    except AssertionError, e:
        return '\033[91m' + 'KK !!!   expected: ' + str(e_res) + ' but got: ' + str(res) + '\033[0m'

algorithms = [selectSortRecursive]
inputs =    [[6,3,0,-1,-3,-5], [-5,-3,-1,0,3,6], [0,-1,-5,6,3,-3], [0,3,-1,-5,6,-3], [3,0,-1,-5,6,-3], [2,1], [1,1,1], [1,2,1,2,1]]
outputs =   [[-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [1,2], [1,1,1], [1,1,1,2,2]]

if __name__ == '__main__':
    print 'Start tests..'
    print len(algorithms), 'algorithms to test'
    print len(inputs), 'tests to conduct'
    for i in range(len(algorithms)):
        print 'testing alg:', algorithms[i]
        for j in range(len(inputs)):
            print 'test num:', j+1, myAssert(algorithms[i], inputs[j], outputs[j])
