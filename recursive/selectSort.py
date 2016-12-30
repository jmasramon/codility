def selectSortRecursive(A):
    def findTheIndexOfTheMax(A, n):
        maxim = 0
        for i in range(n):
            if A[i] > A[maxim]:
                maxim = i
        return maxim

    def swapTheMax(A, n, maxim):
        temp = A[n-1]
        A[n-1] = A[maxim]
        A[maxim] = temp

    def putTheMaxAtTheEnd(A, n):
        maxim = findTheIndexOfTheMax(A, n)
        swapTheMax(A, n, maxim)

    def loop(A, n):
        if n == 1:
            return
        else:
            putTheMaxAtTheEnd(A, n)
            loop(A, n-1)

    loop(A, len(A))
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
